<template>
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
            @click="$refs.file.click()"
        >
            Upload Transcript
        </v-btn>
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
            transcript_file: null
        };
    },
    methods: {
        uploadFile() {
            console.log("uploaded a file!")
            this.transcript_file = this.$refs.file.files[0]
            let reader = new FileReader();
            reader.readAsText(this.transcript_file)
            reader.onload = function(){
                var html = reader.result
                console.log("Read the file, attempting to parse")
                var taken_courses = parse_transcript(html)
                // taken_courses.forEach(course => this.$store.commit('addClass', course))
                console.log(taken_courses)

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
