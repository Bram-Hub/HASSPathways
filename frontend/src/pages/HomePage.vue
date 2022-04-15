<template>
    <div>
        <v-container>
            <Breadcrumbs :breadcrumbs="breadcrumbs" />
            <h1>Welcome to the pathways website!</h1><h3>Here you can explore the different pathways RPI has to offer. To get started choose from on of the options below and start exploring your options!</h3>
            <v-btn
                class="button"
                elevation="0"
                tile
                :to="{ name: 'pathways' }"
            >
                <span class="text">Explore the different pathways</span>
            </v-btn>
            <v-btn
                class="button"
                elevation="0"
                tile
                :to="{ name: 'search-classes' }"
            >
                <span class="text">Find a pathway from classes you have taken</span>
            </v-btn>
            <v-btn
                class="button"
                elevation="0"
                tile
                :to="{ name: 'admin-portal' }"
            >
                <span class="text">Come to our Admin and secure portal</span>
            </v-btn>
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
