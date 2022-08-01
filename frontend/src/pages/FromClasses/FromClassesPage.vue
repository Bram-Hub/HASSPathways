<template>
    <div>
        <v-container>
            <Breadcrumbs :breadcrumbs="breadcrumbs" />

            <h1>HASS Pathways From Classes</h1>
            <p>Search for the classes you have taken and then continue to the next page to display the computed pathways for you!</p>

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
                        v-model="import_dialog"
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
                                7. Drag and drop the html document into the box below or press "UPLOAD TRANSCRIPT".
                            </v-card-text>
                            <!-- https://codepen.io/dimitri-lopez/pen/gOeGRGK -->
                           <v-divider />
                           <div id="drop-area" style="text-align: center;">
                               <form class="my-form" >
                                   <p>Drag and drop your unofficial transcript here.</p>
                                   <input type="file" id="fileElem" accept="*\.pdf" onchange="handleFiles(this.files)" style="display: none;">
                                   <label id="upload-button" for="fileElem">Upload Transcript</label>
                               </form>
                               <progress id="progress-bar" max=100 value=0></progress>
                               <div id="gallery" />
                           </div>

                            <v-divider />
                            <v-card-actions>
                                <v-spacer />
                                <v-btn
                                    color="secondary"
                                    class="font-weight-bold"
                                    text
                                    @click="import_dialog = false"
                                >
                                    Cancel
                                </v-btn>
                                <v-btn
                                    color="primary"
                                    class="font-weight-bold"
                                    text
                                    @click="deselectAll(); import_dialog = false"
                                >
                                    Upload Transcript
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
                <h5 style="color: x11gray;" class="ml-4">
                    Current selections ({{ this.selected.length }}):
                    <li v-for="(course, index) in this.selected" :key="(course, index)" style="list-style: none; display: inline;">
                        {{ course.name }}{{ index &lt; selected.length - 1 ? ", " : "" }}
                    </li>
                </h5>
                <v-data-table
                    v-model="selected"
                    :headers="courseHeaders"
                    :items="courses"
                    :single-select="false"
                    :disable-pagination="true"
                    :search="searchValue"
                    :fixed-header="true"

                    sort-by="id"
                    item-key="name"
                    show-select
                    class="elevation-1"
                    hide-default-footer
                    height="400px"
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
                            <td>{{ item.name }}</td>
                        </tr>
                    </template>
                </v-data-table>
            </v-card>
        </v-container>
    </div>
</template>

<script>
import Breadcrumbs from '../../components/Breadcrumbs'
import breadcrumbs from '../../data/breadcrumbs.js'
import { courses } from '../../data/data.js'

const TABLE_HEADERS = [
    {
        text: 'Course Code',
        value: 'identifier',
        width: '130px'
    },
    {
        text: 'Name',
        value: 'name'
    }
];

export default {
    components: {
        Breadcrumbs
    },
    data() {
        const courseList = Object.values(courses).map(course => {
            return {
                name: course.name,
                identifier: course.subj + '-' + course.ID + course['cross listed'].map(el => ' / ' + el).join(""),
            };
        });

        return {
            breadcrumbs: breadcrumbs.from_classes_search,
            searchValue: '',
            courses: courseList,
            courseHeaders: TABLE_HEADERS,
            selected: courseList.filter(course => this.$store.state.classes[course.name]),
            dialog: false,
            import_dialog: false
        }
    },
    methods: {
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
        }
    }
}
</script>
<style>
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


