<template>
    <v-card
        class="rounded-0 card"
        elevation="1"
        :style="{ borderColor: colorHash(pathwayCategory) }"
    >
        <v-card-title class="font-weight-bold text-truncate card-title title-container">
            <span class="title-text text-truncate">
                {{ title }}
            </span>
            <v-icon
                class="menu-icon"
                @click="console.log('tmp')"
            >
                mdi-eye
            </v-icon>
            <v-icon
                class="menu-icon"
                @click="console.log('tmp')"
            >
                mdi-dots-horizontal
            </v-icon>
        </v-card-title>
        
        <div class="classes-container">
            <div
                v-for="key in requiredKeys" :key="key"
                class=""
            >
                <v-subheader class="subheader">
                    {{ requiredKeyNames[key] }}
                </v-subheader>

                <div class="class-items-container">
                    <span
                        v-for="clazz in formatClassCategory(classes[key])"
                        :key="clazz"
                    >
                        <p style="margin: 0">{{ clazz }}</p>
                    </span>
                </div>
            </div>
        </div>
    </v-card>
</template>

<script>
import toMaterialStyle from 'material-color-hash';

const requiredKeys = ['sec1', 'sec2', 'sec3', 'minor'];
const requiredKeyNames = {
    sec1: 'Section 1',
    sec2: 'Section 2',
    sec3: 'Section 3',
    minor: 'Minor'
}

export default {
    name: 'MyPathway',
    props: {
        title: {
            type: String,
            required: true
        },
        classes: {
            type: Object,
            required: true,
            validator: classes =>
                requiredKeys.every(key => Object.keys(classes).includes(key)) && // All required keys included
                requiredKeys.every(key => Array.isArray(classes[key]))
        },
        pathwayCategory: {
            type: String,
            required: true
        }
    },
    data() {
        return { requiredKeys, requiredKeyNames };
    },
    methods: {
        formatClassCategory(classes) {
            if (!classes || !classes.length)
                return ['*No classes*'];
            return classes.slice(0, 2);
        },
        colorHash(text) {
            return toMaterialStyle(text).backgroundColor;
        }
    }
}
</script>

<style scoped lang="scss">
    .card {
        margin: 5px;
        width: 340px;
        height: 450px;

        max-width: 95%;
        max-height: 90%;

        display: inline-flex;
        flex-direction: column;
        vertical-align: top;
        border-top: 3px solid var(--v-primary-base);

        .title-container {
            display: flex;
            flex-wrap: nowrap;
            justify-content: space-between;

            .title-text {
                padding-right: 20px;
                display: inline-block;
                width: 100%;
            }

            .menu-icon {
                margin: 0 8px;
                float: right;
            }
        }

        .subheader {
            // Make divider subheader smaller and no inset
            height: 24px;
            padding-left: 0;
            font-size: 9pt;
            text-transform: uppercase;
        }

        .classes-container {
            padding: 0 20px;
            overflow-y: auto;
            
            .class-items-container {
                margin-bottom: 12px;
            }
        }
    }
</style>
