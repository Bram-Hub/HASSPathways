

<template>
  <div>
    <ProgressBar />
    <v-expansion-panels
      v-if="this.$store.editingCourses == true"
      v-model="panel"
      flat
      outlined
      tile
      accordion
      hover
      multiple
      class="expansion-panel pt-15"
    >
      <v-expansion-panel
        v-for="(path, i) in filteredPathways"
        :key="i"
        @click="selectPathway(path)"
      >
        <v-expansion-panel-header
          id="expansion-header"
          color="#c65353"
        >
          {{ path.pathName }}
          <template #actions>
            <v-icon color="white">
              $expand
            </v-icon>
          </template>
        </v-expansion-panel-header>

        <v-expansion-panel-content>
          <v-card
            flat
            color="#dcdcdc"
          >
            <v-card-text class="mt-4">
              {{ path.pathDescript }}
            </v-card-text>
          </v-card>

          <FirstCourses
            v-if="courseNumber=='first'"
            :path="path"
            @nextBucket="moveToNextBucket"
          />
          <SecondCourses
            v-else-if="courseNumber=='second'"
            :path="path"
            @nextBucket="moveToNextBucket"
          />
          <ThirdCourses
            v-else-if="courseNumber=='third'"
            :path="path"
          />
        </v-expansion-panel-content>
        <v-divider color="white" />
      </v-expansion-panel>
    </v-expansion-panels>

    <v-expansion-panels
      v-if="this.$store.editingCourses != true"
      v-model="panel"
      flat
      outlined
      tile
      accordion
      hover
      multiple
      class="expansion-panel overflow-y-auto"
    >
      <v-expansion-panel
        v-for="(path, i) in filteredPathways"
        :key="i"
        @click="selectPathway(path)"
      >
        <v-expansion-panel-header
          id="expansion-header"
          color="#c65353"
        >
          {{ path.pathName }}
          <template #actions>
            <v-icon color="white">
              $expand
            </v-icon>
          </template>
        </v-expansion-panel-header>

        <v-expansion-panel-content>
          <v-card
            flat
            color="#dcdcdc"
          >
            <v-card-text class="mt-4">
              {{ path.pathDescript }}
            </v-card-text>
          </v-card>

          <FirstCourses
            v-if="courseNumber=='first'"
            :path="path"
            @nextBucket="moveToNextBucket"
          />
          <SecondCourses
            v-else-if="courseNumber=='second'"
            :path="path"
            @nextBucket="moveToNextBucket"
          />
          <ThirdCourses
            v-else-if="courseNumber=='third'"
            :path="path"
          />
        </v-expansion-panel-content>
        <v-divider color="white" />
      </v-expansion-panel>
    </v-expansion-panels>
    <div>
      <v-btn
        v-if="courseNumber=='third' || this.$store.editingCourses == true"
        id="button1"
        large
        fixed
        bottom
        right
        fab
        class="stickyButton"
@click="savePathway()"
      >
        <v-icon style="color: white">
          mdi-content-save
        </v-icon>
      </v-btn>
    </div>
  </div>
</template>

<script>

import ProgressBar from '../ProgressBar/ProgressBar.vue'
import FirstCourses from '../FirstCourses'
import SecondCourses from '../SecondCourses'
import ThirdCourses from '../ThirdCourses'
import pJson from '../../../../JSONfiles/pathways.json'
import cJson from '../../../../JSONfiles/courses.json'
import { mapGetters, mapMutations } from 'vuex'

export default {
  components: {
    FirstCourses,
    SecondCourses,
    ThirdCourses,
    ProgressBar,
  },
  data() {
    return {
      pathways: pJson,
      coursesJson: cJson,
      courseNumber: 'first',
      savedCourses: [],
      filter: '',
      panel: []
    }
  },
  methods: {
    ...mapGetters(['course1',`course2`,`course3`]),
    ...mapMutations(['setSelectedPathway','saveButton', 'removePath']),
    pathwayExist(courseCombo){
      for (var i = 0; i < this.$store.getters.getOptions.length; i++) {
        if (this.$store.getters.getOptions[i][1] == courseCombo[0].fields.name &&
          this.$store.getters.getOptions[i][2] == courseCombo[1].fields.name &&
          this.$store.getters.getOptions[i][3] == courseCombo[2].fields.name) {
            console.log("exists")
            return true
        }
      }
      console.log("does not exist")
      return false
    },
    savePathway(){
      // If the third course has been chosen or not
      if (this.$store.getters.thirdCourse){
        // If the pathway already exists reject save
        if (this.pathwayExist([this.$store.getters.firstCourse, this.$store.getters.secondCourse, this.$store.getters.thirdCourse])) {
          if (this.$store.editingCourses == true){
            this.$store.editingCourses = false
            this.$store.targetEditIndex = -1
          }
          this.$toast.clear()
          this.$toast.error("This pathway already exists!", {
            position: "top-right",
            timeout: 3000,
            pauseOnFocusLoss: true,
            hideProgressBar: true,
            rtl: false,
            closeButton: "button",
          });
          this.$root.$emit('resetProgress')
        }else{
          if (this.$store.editingCourses == true){
            this.removePath(this.$store.targetEditIndex)
            this.$store.editingCourses = false
            this.$store.targetEditIndex = -1
          }
          this.saveButton()
          this.$root.$emit('resetProgress')
          this.$toast.clear()
          this.$toast.success("Saved Pathway!", {
            position: "top-right",
            timeout: 3000,
            pauseOnFocusLoss: true,
            hideProgressBar: true,
            rtl: false,
            closeButton: "button",
          });
        }
      }else{
        this.$toast.clear()
        this.$toast.error("You haven't chosen three courses yet!", {
          position: "top-right",
          timeout: 3000,
          pauseOnFocusLoss: true,
          hideProgressBar: true,
          closeButton: "button",
        });
      }
      this.$root.$emit(`closePanels`)
    },
    selectPathway(path) {
      
      this.setSelectedPathway(path.pathName)
      console.log(this.$store.getters.pathway)
    },
    moveToNextBucket(course) {
      this.courseNumber = course
      if (this.courseNumber == "first") {
        this.$root.$emit('changeWhichCourse', "first")
      } else if (this.courseNumber == "second") {
        this.$root.$emit('changeWhichCourse', "second")
      } else if (this.courseNumber == "third") {
        this.$root.$emit('changeWhichCourse', "third")
      }
    }
  },
  mounted() {
    this.$root.$on('changeWhichCourse', (course) => {
      this.courseNumber = course
    }),
    this.$root.$on('changedFilter', (input) => {
      this.filter = input
    }),
    this.$root.$on('closePanels', () => {
      this.panel = []
    }),
    this.courseNumber = this.bucketNumber;
  },
  computed: {
    ...mapGetters(['pathway', 'firstCourse', 'secondCourse', 'thirdCourse']),
    filteredPathways() {
      var pathwayObj = this.pathways
      //var allCourses = this.coursesJson
      var result = []
      //Loop through pathway objects
      for (var modelKey in pathwayObj) {
        if (this.courseNumber != "first"){
          if (pathwayObj[modelKey].fields.pathName == this.$store.getters.pathway){
            result[0] = pathwayObj[modelKey].fields
          }
        }else{
          var model = pathwayObj[modelKey].fields
          result[modelKey] = model 
        }
      }
    return result
    },
    bucketNumber() {
      if (this.$store.getters.firstCourse != null) {
        if (this.$store.getters.secondCourse != null) {
          if (this.$store.getters.thirdCourse != null) {
            return 'third'
          }
          return 'third'
        }
        return 'second'
      }
      return 'first'
    }
  }
}
</script>

<style scoped>
  @import "ExpansionPanel.scss";
</style>
