<template>
    <diagram :model="model" />
</template>
<script>
import { Diagram } from 'vue-diagrams';

export default {

    components: {
        Diagram
    },
    data() {
        const diagramModel = new Diagram.Model();

        const class1 = diagramModel.addNode("Class1", 0, 0);
        const class1out = class1.addOutPort("out");

        const class2 = diagramModel.addNode("Class2", 300, 0);
        const class2in = class2.addInPort("in");
        const class2out = class2.addOutPort("out");

        const class3 = diagramModel.addNode("Class3", 600, 0);
        const class3in = class3.addInPort("in");

        diagramModel.addLink(class1out, class2in);
        diagramModel.addLink(class2out, class3in);

        return {
            model: diagramModel
        };
    },
};
</script>
