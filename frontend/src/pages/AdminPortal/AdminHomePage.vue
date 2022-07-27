<template>
    <div>
        <v-container>
            <Breadcrumbs :breadcrumbs="breadcrumbs" />
            <h1>Welcome to the Admin Portal!</h1>
            <p>Here you can edit the courses and pathways on the website!</p>
            <v-divider class="my-4" />
            <ul id="btn-cntnr">
                <v-btn id="admn-btn" :to="{ name: 'admin-pathway' }" class="text-decoration-none">
                    <v-icon left dark>
                        mdi-magnify
                    </v-icon>
                    Search for a class by pathway
                </v-btn>
                <v-btn id="admn-btn" :to="{ name: 'admin-search-course-code' }" class="text-decoration-none">
                    <v-icon left dark>
                        mdi-book-edit
                    </v-icon>
                    Edit a class by course code
                </v-btn>
                <v-btn id="admn-btn" :to="{ name: 'admin-course' }" class="text-decoration-none">
                    <v-icon left dark>
                        mdi-book-plus
                    </v-icon>
                    Add a new course to the website
                </v-btn>
            </ul>
        </v-container>
    </div>
</template>

<script>
import Breadcrumbs from '../../components/Breadcrumbs'
import breadcrumbs from '../../data/breadcrumbs.js'

export default {
    components: {
        Breadcrumbs
    },
    data() {
        return {
            breadcrumbs: breadcrumbs.admin_home_page
        }
    }
}
</script>

<style scoped>
#btn-cntnr {
    padding: 0px !important;
    text-align: center;
}
#admn-btn {
    list-style: none;
    text-align: center;
    display: inline-block;
    background-color: #f73e3e;
    margin: 0px 1vw 1vw 0px;
    height: 50px;
    max-width: 100%;
    color: white;
    font-size: 14px !important;
    padding-top: 15px;
}

@media only screen and (min-width: 600px) {
    #admn-btn {
        list-style: none;
        text-align: center;
        display: inline-block;
        background-color: #f73e3e;
        margin: 0px 1vw 1vw 0px;
        height: 50px;
        max-width: 900px;
        color: white;
        font-size: 15px !important;
        padding-top: 15px;
    }

}
</style>
