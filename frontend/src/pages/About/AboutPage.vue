<template>
    <div>
        <v-container>
            <Breadcrumbs :breadcrumbs="breadcrumbs" />
            <h1>What are HASS integrative pathways?</h1>
            <p>Every undergraduate student at RPI must fulfill the pathway requirement. The pathway is a way to both guide students towards choosing courses and also enrich their HASS core. The pathways can vary from interdisciplinary to focused within one subject area. Each pathway consists of a 12-credit concentration of courses. </p>
            <h2>FAQ</h2>
            <ul>
                <li>
                    <h4>Do I need to take an IHSS for my pathway?</h4>
                    <p>Taking an IHSS course is not a requirement for pathways, but for the overall HASS requirement. Although some pathways might require a specific IHSS course.</p>
                </li>
                <li>
                    <h4>Do I need to take a 4000 level course for my pathway?</h4>
                    <p>Check the individual pathway requirements. Some pathways might require one course to be 4000 level and some might not.</p>
                </li>
                <li>
                    <h4>Do I need to take a communication intensive course for my pathway?</h4>
                    <p>This is not a requirement for the pathway.</p>
                </li>
                <li>
                    <h4>Am I allowed to come up with my own pathway?</h4>
                    <p>Students are not allowed to create their own pathway.</p>
                </li>
                <li>
                    <h4>Can my pathway courses count towards a minor?</h4>
                    <p>Yes, lots of pathways even have an associated minor which sometimes might only require one more course to achieve.</p>
                </li>
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
            breadcrumbs: breadcrumbs.about_page

        }
    }
}
</script>