<template>
    <div style="width: 75%; margin: 0 auto;">
        <v-container fluid>
            <Breadcrumbs :breadcrumbs="breadcrumbs" />
            <h1>Welcome to HASS Pathways!</h1>
            <p>Here you can explore the different pathways RPI has to offer. To get started choose from on of the options below and start exploring your options!</p>
            <v-divider class="my-4" />
            
            <div style="text-align: center">
                <v-btn
                    class="button pathway-btn [ mr-2 mt-2 font-weight-bold ]"
                    elevation="0"
                    color="primary"
                    tile
                    x-large
                    :to="{ name: 'pathways' }"
                >
                    <v-icon left dark>
                        mdi-compass
                    </v-icon>
                    <span class="text">Explore pathways</span>
                </v-btn>
                <v-btn
                    class="button pathway-btn [ mr-2 mt-2 font-weight-bold ]"
                    color="primary"
                    elevation="0"
                    tile
                    x-large
                    :to="{ name: 'search-classes' }"
                >
                    <v-icon left dark>
                        mdi-magnify
                    </v-icon>
                    <span class="text" style="display: block">Find pathways from classes</span>
                </v-btn>

                <br>
                <v-btn
                    class="button mt-4"
                    elevation="0"
                    tile
                    :to="{ name: 'admin-portal' }"
                >
                    <v-icon left dark>
                        mdi-cog
                    </v-icon>
                    <span class="text">Admin and secure portal</span>
                </v-btn>
            </div>
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
    min-width: 330px !important;
    max-width: 92vw !important;
    overflow-x: hidden;
    margin-bottom: 5px;
}
</style>
