<template>
    <v-container class="d-flex align-center justify-center flex-column" style="height: 100%">
        <h1 class="title-404">
            404 Page Not Found
        </h1>
        <p class="subtitle-404">
            The page you are looking for has moved, or doesn't exist.
        </p>

        <v-btn
            class="mt-4"
            color="primary"
            to="/pathways"
        >
            Go to Homepage
        </v-btn>
    </v-container>
</template>

<script>
export default {
    name: 'Four0FourPage'
}
</script>

<style scoped>
.title-404 {
    font-size: 4rem;
}

.subtitle-404 {
    font-size: 1.2rem;
}
</style>
