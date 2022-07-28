<template>
  <div class="uk-container">
    <h3>TreeView</h3>
    <div>
      <div v-if="data.type==='directory'">
        <TreeDirectory :name="data.name" :children="data.children"></TreeDirectory>
      </div>
      <div v-else>
        <TreeFile :name="data.name"></TreeFile>
      </div>
    </div>
  </div>
</template>

<script>
// @ is an alias to /src
// import HelloWorld from '@/components/HelloWorld.vue'

import TreeForm from '@/assets/dir.json';
import TreeDirectory from '@/components/TreeView/TreeDirectory.vue';
import TreeFile from '@/components/TreeView/TreeFile.vue';

export default {
  data() {
    return {
      treeForm: TreeForm,
      data: {},
    }
  },
  methods: {
    createLayer() {

    }
  },
  created() {
    for (let value in this.treeForm) {
      if (value === 'name') {
        this.data.name = this.treeForm[value];
      }
      if (value === 'type') {
        this.data.type = this.treeForm[value];
      }
      if (value === 'children') {
        this.data.children = this.treeForm[value];
      }
    }
    console.log(this.data);
  },
  components: {
    TreeDirectory,
    TreeFile,
  }
}
</script>

<style>

</style>



<style>
.home
{
  grid-column-start: 5;
  grid-column-end: 7;
  grid-row-start: 1;
  grid-row-end: 3;
  align-self: stretch;
  text-align: center;
}

.info{
  grid-column-start: 5;
  grid-column-end: 7;
  grid-row-start: 1;
  grid-row-end: 3;
  font-size:x-large;

}

.home-table{

  grid-column-start: 5;
  grid-column-end: 7;
  grid-row-start: 1;
  grid-row-end: 3;
  align-self: stretch;
  text-align: left;
  font-size: medium
}

</style>

