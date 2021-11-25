<template>
    <v-breadcrumbs :items="breadcrumbs" class="px-0">
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
