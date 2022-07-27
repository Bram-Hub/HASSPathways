<template>
    <div id="course">
        <hr/>
        <h4>
            {{course[0].name}}
        </h4>
        <hr/>
        <div id="courseDesc">
            {{course[0].description}}
        </div>
    </div>
</template>
<script>
export default {
    props: {
        course: {
            type: Object,
            required: true,
        },
        pathwayId: {
            type: String,
            required: false,
            default: null
        }
    },
}
</script>

<style>
</style>