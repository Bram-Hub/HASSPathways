<template>
    <span class="bookmark-holder">
        <v-tooltip v-if="bookmarkSelected" bottom>
            <template #activator="{on, attrs}">
                <v-icon 
                    class="selected" 
                    v-bind="attrs" 
                    large
                    v-on="on" 
                    @click="deselectBookmark()" 
                >
                    mdi-bookmark
                </v-icon>
            </template>
            <span>Remove pathway from "My Pathways"</span>
        </v-tooltip>
        <v-tooltip v-else bottom>
            <template #activator="{on, attrs}">
                <v-icon 
                    class="unselected" 
                    v-bind="attrs" 
                    large
                    v-on="on"  
                    @click="selectBookmark()" 
                >
                    mdi-bookmark-outline
                </v-icon>
            </template>
            <span>Add pathway to "My Pathways"</span>  
        </v-tooltip>
    </span>
</template>

<script>

export default {
    name: 'Bookmark',
    props: {
        pathwayId: {
            type: String,
            required: true
        },
    },
    data() {
        return {
            bookmarkSelected: false
        }
    },
    mounted() {
        this.bookmarkSelected = this.bookmarked;
    },
    computed: {
        bookmarked() {
            return this.$store.getters.pathwayBookmarked(this.pathwayId);
        }
    },
    methods : {
        selectBookmark() { 
            this.bookmarkSelected = !this.bookmarkSelected;
            console.log(this.pathwayId);
            this.$store.commit('bookmarkPathway', this.pathwayId);
        },
        deselectBookmark() { 
            this.$store.commit('unBookmarkPathway', this.pathwayId);
            this.bookmarkSelected = !this.bookmarkSelected;
        }
    }
}
</script>


<style scoped>
.bookmark-holder {
    display: inline-flex;
    top: 0;
    cursor: pointer;
    z-index: 9;
}
</style>