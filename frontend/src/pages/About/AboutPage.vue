<template>
    <div>
        <v-container>
            <Breadcrumbs :breadcrumbs="breadcrumbs" />
            <h1>What are HASS integrative pathways?</h1>
            <p>Every undergraduate student at RPI must fulfill the pathway requirement. The pathway is a way to both guide students towards choosing courses and also enrich their HASS core. The pathways can vary from interdisciplinary to focused within one subject area. Each pathway consists of a 12-credit concentration of courses. </p>
            <p>See <a style="text-decoration: none" href="http://catalog.rpi.edu/">RPI Catalog</a> and <a style="text-decoration: none" href="https://hass.rpi.edu/advising/hass-integrative-pathways/">HASS website</a> for the official details about pathways.</p>

            <h2><i>Frequently Asked Questions</i></h2>
            <div class="buttons">
                <v-btn @click="all">
                    open all
                </v-btn>
                <v-btn @click="none">
                    close all
                </v-btn>
            </div>
            <div>
                <!-- List of all asked questions fetched from backend -->
                <v-expansion-panels v-model="panel"
                                    multiple focusable>
                    <v-expansion-panel
                                       v-for="(a, q) in faqs"
                                       :key="a">
                        <v-expansion-panel-header>
                            <!-- 'question' goes here -->
                            {{q}}
                        </v-expansion-panel-header>
                        <v-expansion-panel-content> 
                            <!-- answer goes in here -->
                            {{a}}
                        </v-expansion-panel-content> 
                    </v-expansion-panel> 
                </v-expansion-panels>
            </div>
        </v-container>
    </div>
</template>
    
<script>
    import Breadcrumbs from '../../components/Breadcrumbs'
    import breadcrumbs from '../../data/breadcrumbs.js'
    import axios from 'axios'
    import Vue from 'vue'

    axios.defaults.baseURL = 'http://129.161.36.233:5000'
    Vue.prototype.$ajax = axios

    export default {
        components: {
            Breadcrumbs
        },
        data() {
            return {
                breadcrumbs: breadcrumbs.about_page,
                panel: [],
                faqs: {},
            }
        },

        // full disclosure that this code was taken from the vue documentation
        // https://vuetify.cn/en/components/expansion-panels/
        methods: {
            // Create an array the length of the items
            // with all values as true
            all() {
                let n_questions = Object.keys(this.faqs).length;
                this.panel = [...Array(n_questions).keys()];    //form a list [0, 1, ... number of questions-1]
            },
            // Reset the panel
            none() {
                this.panel = [];
            },
            getFaqs() {
                this.$ajax.get('/faqs', {}).then(res => {
                    this.faqs = res.data.questions;
                })
            }
        },
        mounted() {
            this.getFaqs();
        }
    }
</script>

<style scoped>
    .buttons {
      padding: 10px 0;
      display: grid;
      justify-items: left;
      align-items: center;
      grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
      grid-gap: 10px;
      display: flex;
      flex-wrap: wrap;
      justify-content: left;
}

.v-expansion-panel-content>>> .v-expansion-panel-content__wrap {
  padding: 10px !important;
}
</style>