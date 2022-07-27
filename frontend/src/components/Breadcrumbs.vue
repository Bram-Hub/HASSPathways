<template>
    <v-breadcrumbs large :items="breadcrumbs" class="px-0 breadcrumb-padding">
        <template #divider>
            <v-icon>mdi-chevron-right</v-icon>
        </template>
    </v-breadcrumbs>
</template>

<script>
export default {
    name: 'Breadcrumbs',
    props: {
        breadcrumbs: {
            type: Array,
            required: true,
            validator: val => val.every(crumb =>
                ['href', 'text'].every(k => Object.keys(crumb).includes(k)))
        }
    },
}
</script>

<style scoped>
.breadcrumb-padding {
    padding-top: 0px;
    padding-bottom: 8px;
    font-size: large;
}
</style>
