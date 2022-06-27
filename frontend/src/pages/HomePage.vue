<template>
    <div style="width: 75%; margin: 0 auto;">
        <v-container fluid>
            <Breadcrumbs :breadcrumbs="breadcrumbs" />
            <h1 style="text-align: center;">
                Welcome to HASS Pathways!
            </h1>
            <p style="text-align: center;">
                Here you can explore the different pathways RPI has to offer. To get started choose from on of the options below and start exploring your options!
            </p>
            <v-divider class="my-4" />
            <v-row
                align="center"
                justify="space-around"
            >
                <v-btn
                    pathway-btn
                    large
                    color="primary"
                    :to="{ name: 'pathways' }"
                >
                    <v-icon left dark>
                        mdi-compass
                    </v-icon>
                    Explore pathways
                </v-btn>
                <v-btn
                    pathway-btn
                    large
                    color="primary"
                    :to="{ name: 'search-classes' }"
                >
                    <v-icon left dark>
                        mdi-magnify
                    </v-icon>
                    Find pathways from classes
                </v-btn>
                <v-btn
                    pathway-btn
                    large
                    color="primary"
                    :to="{ name: 'about' }"
                >
                    <v-icon left dark>
                        mdi-help-circle-outline
                    </v-icon>
                    Learn about Pathways
                </v-btn>
                <v-btn
                    pathway-btn
                    large
                    :to="{ name: 'admin-portal' }"
                >
                    <v-icon left dark>
                        mdi-cog
                    </v-icon>
                    <span v-if="!$vuetify.theme.dark" class="text" id="admin">Admin and secure portal</span>
                   <span v-else class="text">Admin and secure portal</span>
                    
                </v-btn>
            </v-row>
        </v-container>
    </div>
</template>

<script>
import Breadcrumbs from '../components/Breadcrumbs'
import breadcrumbs from '../data/breadcrumbs.js'

export default {
    components: {
        Breadcrumbs
    },
    data() {
        return {
            breadcrumbs: breadcrumbs.home
        }
    }
}
</script>

<style scoped>
.pathway-btn {

    width: 40%;
    min-width: 400px !important;



    overflow-x: hidden !important;
    width: 40%;
    max-width: 92vw !important;
    overflow-x: hidden;
    margin-bottom: 5px;
 }

#admin {
    font-weight: bold;
}

</style>
