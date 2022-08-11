<template>
    <div>
        <div id="drop-area" style="text-align: center;">
            <p>Drag and drop your unofficial transcript here.</p>
            <input
                id="fileInput"
                ref="file"
                type="file"
                accept=".html"
                style="display: none;"
                @change="uploadFile"
            >
            <v-btn
                color="green"
                class="mr-2 font-weight-bold mobile-btn white--text"
                @click="$refs.file.click()"
            >
                Upload Transcript
            </v-btn>
        </div>
        <span>
            Imported Classes: {{imported_classes_str}}
        </span>
    </div>
</template>

<script>
// import UploadService from "../services/UploadFilesService";
import JSSoup from 'jssoup';
import {parse_transcript} from "../../../backend/scrapers/transcript_scraper.js"
export default {
    name: 'UploadTranscript',
    data() {
        return {
            transcript_file: null,
            taken_courses: [],
            imported_classes_str: ""

        };
    },
    methods: {
        uploadFile() {
            this.transcript_file = this.$refs.file.files[0]
            let reader = new FileReader();
            reader.readAsText(this.transcript_file)
            var instance = this
            var taken_courses = this.taken_courses
            reader.onload = function(){
                var html = reader.result
                taken_courses = parse_transcript(html)
                // console.log("courses: " + taken_courses)
                taken_courses.forEach(course => instance.$store.commit('addClass', course))
                instance.$emit("imported_classes")
                instance.imported_classes_str = taken_courses.join(", ")
            }
        }
    }

}
</script>

<style scoped>
#drop-area {
  border: 2px dashed #ccc;
  border-radius: 20px;
  width: 480px;
  margin: 20px auto;
  padding: 20px;
}
#drop-area.highlight {
  border-color: #4CAF50;
}
#upload-button {
    display: inline-block;
    padding: 10px;
    background: #4CAF50;
    color: white;
    cursor: pointer;
    font-weight: medium;
    border-radius: 5px;
    border: 1px solid #ccc;
}
#upload-button:hover {
    /* TODO fix the color on this */
    background: #4CAE6F;
}

</style>
