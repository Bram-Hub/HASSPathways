<template>
    <div>
        <v-container>
            <Breadcrumbs :breadcrumbs="breadcrumbs" />

            <h1>HASS Pathways From Classes</h1>
            <p>Search for the classes you have taken and then continue to the next page to display the computed pathways for you!</p>

            <p>Try searching for all non-digital art classes offered in the fall at the 2,000 level by searching "arts fall 2000 ! digital".</p>
            <v-card outlined tile>
                <v-card-title>
                    <v-text-field
                        v-model="searchValue"
                        append-icon="mdi-magnify"
                        label="Search"
                        single-line
                        hide-details
                        dense outlined
                        style="border-radius: 0"
                    />
                    <v-spacer />
                    <!-- Clear confirmation modal -->
                    <v-dialog
                        v-model="transcript_dialog"
                        width="700"
                        light
                        overlay-opacity="0.8"
                    >
                        <template #activator="{ on, attrs }">
                            <v-btn
                                dark
                                color="blue" outlined tile
                                class="mr-2 font-weight-bold mobile-btn"
                                v-bind="attrs"
                                v-on="on"
                            >
                                Import Classes
                                <v-icon right>
                                    mdi-upload
                                </v-icon>
                            </v-btn>
                        </template>
                        <v-card>
                            <v-card-text class="pt-4 font-weight-medium">
                                <h3 class="mb-1">
                                    Uploading Your Unofficial Web Transcript
                                </h3>
                                This will take your unofficial transcript
                                available on SIS and import all the HASS classes
                                on it. This will allow you to see what pathways
                                are compatible for the classes you have already
                                taken.
                                <br>
                                <br>
                                If your classes already appear under the
                                <b>Imported Classes</b> section below, simply
                                press "SELECT IMPORTED CLASSES" to select them.
                                No need to reupload your transcript!
                                <br>
                                <br>
                                In order to upload your transcript:
                                <br>
                                1. Log onto <a href="https://sis.rpi.edu" target="_blank">https://sis.rpi.edu</a>.
                                <br>
                                2. Go to the "Student Menu".
                                <br>
                                3. Under "Curriculum Information" click "View Transcript".
                                <br>
                                4. Select "All Levels" for the level and "Unoficial Web Transcript" for the type and then click submit.
                                <br>
                                5. Press Ctrl+s or right click a blank spot on the page and select "Save as...".
                                <br>
                                6. Save the html document.
                                <br>
                                7. Press "UPLOAD TRANSCRIPT" and select your transcript file.
                            </v-card-text>
                            <v-divider />
                            <UploadTranscript />
                            <v-divider />
                            <v-card-actions>
                                <v-spacer />
                                <v-btn
                                    color="secondary"
                                    class="font-weight-bold"
                                    text
                                    @click="transcript_dialog = false"
                                >
                                    Cancel
                                </v-btn>
                                <v-btn
                                    color="primary"
                                    class="font-weight-bold"
                                    text
                                    @click="transcript_dialog = false; selectTranscriptClasses()"
                                >
                                    Select Imported Classes
                                </v-btn>
                            </v-card-actions>
                        </v-card>
                    </v-dialog>


                    <v-dialog
                        v-model="dialog"
                        width="500"
                        light
                        overlay-opacity="0.8"
                    >
                        <template #activator="{ on, attrs }">
                            <v-btn
                                color="red" outlined tile
                                class="mr-2 font-weight-bold mobile-btn"

                                v-bind="attrs"
                                v-on="on"
                            >
                                Clear Selections <v-icon right>
                                    mdi-close-circle-outline
                                </v-icon>
                            </v-btn>
                        </template>
                        <v-card>
                            <v-card-text class="pt-4 font-weight-medium">
                                <h3 class="mb-1">
                                    Are you sure?
                                </h3>
                                You are about to unselect all your classes.
                            </v-card-text>
                            <v-divider />
                            <v-card-actions>
                                <v-spacer />
                                <v-btn
                                    color="primary"
                                    class="font-weight-bold"
                                    text
                                    @click="dialog = false"
                                >
                                    Cancel
                                </v-btn>
                                <v-btn
                                    color="primary"
                                    class="font-weight-bold"
                                    text
                                    @click="deselectAll(); dialog = false"
                                >
                                    Unselect all
                                </v-btn>
                            </v-card-actions>
                        </v-card>
                    </v-dialog>

                    <!-- Next button -->
                    <v-btn 
                        dark
                        color="green" tile
                        to="/from-classes"
                        class="mr-2 font-weight-bold mobile-btn"
                    >
                        Find Pathways <v-icon right>
                            mdi-arrow-right-circle
                        </v-icon>
                    </v-btn>
                </v-card-title>
                <h5 style="color: white;" class="ml-4">
                    Current selections ({{ this.selected.length }}):
                    <li v-for="(course, index) in this.selected" :key="(course, index)" style="list-style: none; display: inline;">
                        {{ course.name }}{{ index &lt; selected.length - 1 ? ", " : "" }}
                    </li>
                </h5>
                <v-data-table
                    v-model="selected"
                    :headers="courseHeaders"
                    :items="filteredCourses"
                    :single-select="false"
                    :fixed-header="true"

                    multi-sort
                    sort-by="Subject"
                    item-key="name"
                    show-select
                    class="elevation-1 pb-6"
                    height="550px"
                    max-height="90%"
                    mobile-breakpoint="10"
                >
                    <!-- Remove select all / unselect all button to prevent
                         users accidentally clearing their selections -->
                    <template #header.data-table-select />

                    <!-- Override default row HTMl so we can add ripples + custom click stuff -->
                    <template #item="{ item, isSelected, select }">
                        <tr 
                            v-ripple
                            :class="'table-row ' + (isSelected ? 'table-row_selected' : '')"
                            @click="rowClick(item, select, isSelected)"
                        >
                            <td>
                                <v-simple-checkbox 
                                    v-ripple color="primary"
                                    :value="isSelected"
                                    @input="rowClick(item, select, isSelected)" 
                                />
                            </td>

                            <td>{{ item.identifier }}</td>
                            <td><a :href="`/course?course=${encodeURIComponent(item.name)}`" class="text-decoration-none"> {{ item.name }} </a></td>
                            <td style="text-align: right;">
                                <SearchTableModifiers class="mt-4 class-card__subtitle__modifiers float-top"
                                                      :course="item" />
                            </td>
                        </tr>
                    </template>
                </v-data-table>
            </v-card>
        </v-container>
    </div>
</template>

<script>
import Breadcrumbs from '../../components/Breadcrumbs'
import UploadTranscript from '../../components/UploadTranscript'
import SearchTableModifiers from '../../components/SearchTableModifiers'
import breadcrumbs from '../../data/breadcrumbs.js'

const TABLE_HEADERS = [
    {
        text: 'Subject',
        value: 'Subject',
    },
    {
        text: 'ID',
        value: 'ID'
    },
    {
        text: 'Name',
        value: 'name'
    },
    {
        text: 'Properties',
        align: 'end',
        sortable: false,
        value: ''
    }
];

export default {
    components: {
        Breadcrumbs,
        UploadTranscript,
        SearchTableModifiers
    },
    data() {
        return {
            breadcrumbs: breadcrumbs.from_classes_search,
            searchValue: '',
            courseHeaders: TABLE_HEADERS,
            dialog: false,
            transcript_dialog: false,
            selected: [],
            coursesData: {},
            chip_names: ["CI", "HI", "Fall", "Spring", "Summer"]
        }
    },
    computed: {
        courses() {
            return Object.values(this.coursesData).map(course => {
                if(course.ID && course['cross listed'] && course.properties && course.offered) {
                    return {
                        name: course.name,
                        Subject: course.subj,
                        ID: course.ID,
                        CI: course.properties.CI,
                        HI: course.properties.HI,
                        Fall: course.offered.fall,
                        Spring: course.offered.spring,
                        Summer: course.offered.summer,
                        search_string: course.subj + '-' + course.ID // course subj-id
                            + course['cross listed'].map(el => ' / ' + el).join("") // cross listed subj-id
                            + " " + course.name // course name
                            + " " + course.ID[0] + "000" // what level is the course
                            + (course.offered.fall ? " Fall" : "")
                            + (course.offered.spring ? " Spring" : "")
                            + (course.offered.summer ? " Summer" : "")
                            + (course.properties.CI ? " COMMUINT" : "")
                            + (course.properties.HI ? " HASSINQ" : "")
                    };
                }
            });
        },
        filteredCourses() {

            // Collapse extra exlamation marks
            let str_array = this.searchValue.split("!")
            for(let i = 2; i < str_array.length; i++){
                str_array[1] += str_array[i]
            }
            let searchText = str_array.join("!")
            let words = searchText.split(/ *! */)
            if(words.length == 1) words.push("")
            let search_words = words[0].split(/ +/)
            let negated_words = words[1].split(/ +/)
            // console.log("search_words: " + search_words)
            // console.log("negated_words: " + negated_words)
            this.add_look_term(search_words, "(?=.*")  //wrap words in a lookahead
            this.add_look_term(negated_words, "(?!.*") //wrap words in a negative lookahead
            // console.log("search: " + negated_words.join("") + search_words.join(""))
            // console.log("-----------------")


            const re = new RegExp(search_words.join("") + negated_words.join(""), 'i') // i is to ignore case sensitive search
            console.log(this.courses.filter(course => course ? re.test(course.search_string) : false));
            return this.courses.filter(course => course ? re.test(course.search_string) : false)
        }
    },
    created() {
        const year = this.$store.state.year;
        import('../../data/json/' + year + '/courses.json').then((val) => {
            this.coursesData = Object.freeze(val);
            let temp = this.courses.filter(course => course != null);
            this.selected = temp.filter(course => this.$store.state.classes[course.name]);
        });
    },
    methods: {
        selectTranscriptClasses(){
            this.$store.commit("addTranscriptClasses")

            let temp = this.courses.filter(course => course != null);
            this.selected = temp.filter(course => this.$store.state.classes[course.name]);
        },
        // On row click, toggle selected state
        rowClick: function (item, select, isSelected) {
            // Is selected is previous selection state
            // So if isSelected is false, then that means the box is checked
            select(!isSelected);

            if (!isSelected) { // The user just checked
                this.$store.commit('addClass', item.name);
            } else {
                this.$store.commit('delClass', item.name);
            }
        },

        deselectAll() {
            this.selected = [];
            this.$store.commit('clearClasses');
        },

        //Surrounds words in a term like "(?=.*word)" which is a positive lookahead
        add_look_term(words, term){
            for (let i = 0; i < words.length; i++) {
                // Remove zero length strings
                if(words[i].length == 0) {
                    words.splice(i, 1)
                    i--;
                    continue;
                }
                if(words[i].toLowerCase().trim() == 'hi') words[i] = "HASSINQ"
                if(words[i].toLowerCase().trim() == 'ci') words[i] = "COMMUINT"
                words[i] = term + words[i] + ")"
            }
        }
    }
}
</script>
<style>
@media only screen and (max-width: 600px) {
    /* Taller rows = easier to click on mobile (only for small screens) */
    .v-data-table > .v-data-table__wrapper > table > tbody > tr > td,
    .v-data-table > .v-data-table__wrapper > table > thead > tr > td,
    .v-data-table > .v-data-table__wrapper > table > tfoot > tr > td {
        height: 64px !important;
    }

    /* On mobile, add vertical margins + full width */
    .mobile-btn {
        width: 100%;
        margin-top: 10px;
    }
}

.table-row { cursor: pointer; }
.table-row_selected { background-color: rgba(229, 57, 53, 0.15); }

::-webkit-scrollbar { 
    width: 13px;
}

::-webkit-scrollbar-track {
    background: lightgray;
}

::-webkit-scrollbar-thumb {
    background: darkgray; /* note: darkgray is lighter than gray */
    border-radius: 1px;
}

::-webkit-scrollbar-thumb:hover {
    background: gray;
}


</style>


