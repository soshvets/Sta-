<template>
  <div class="uk-container">
    <p>{{name}}</p>
    <div v-for="item, index in children" :key="index">
      <div v-if="item.type==='file'">
        <TreeFile :name="item.name"></TreeFile>
      </div>
       <div v-else>
        <TreeDirectory :name="item.name" :children="item.children">
        </TreeDirectory>
    </div>
    </div>
  </div>
</template>

<script>
import TreeFile from './TreeFile.vue'

export default {
  name: 'TreeDirectory',
  data() {
    return {
      
    }
  },
  props: {
    children: {},
    name: String,
  },
  components: {
    TreeFile,
  }
}
</script>

<style>

</style>
