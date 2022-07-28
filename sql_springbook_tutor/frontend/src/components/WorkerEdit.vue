<template>
  <div>

    <p>I am here</p>


    <div class="workeritem uk-card-small uk-card-body  ">

      <form enctype="multipart/form-data" @submit="updateData">
        <label for="first_name" class="uk-form-label">PESEL: </label>
        <input class="uk-input uk-form-controls" type="text" v-model="ob.pesel">
        <label for="first_name" class="uk-form-label">First name: </label>
        <input class="uk-input uk-form-controls" type="text" v-model="ob.name">
        <label for="last_name" class="uk-form-label">Last name: </label>
        <input class="uk-input uk-form-controls" type="text" v-model="ob.surname">
        <label for="age" class="uk-form-label">Age: </label>
        <input class="uk-input uk-form-controls" type="number" v-model="ob.age">

        <button type="submit" class="uk-button uk-button-default uk-width-1-1@s">Update</button>
      </form>

    </div>
  </div>

</template>

<script>
import Vue from 'vue';
import axios from '@/lib/http-common'
import VueAxios from 'vue-axios';

Vue.use(VueAxios, axios)

export default {
  props: ['workeritem'],

  data() {
    return {

      ob: {}
    }
  },
  mounted() {

    this.updateData()

  },
  methods: {

    async updateData() {
      if (this.ob.name != "" && this.ob.surname != "" && this.ob.age > 0) {

        console.log(this.ob);
        try {
          await axios.put(`/workers/update`, this.ob, { headers: { 'Content-Type': 'application/json' } });
        }
        finally {
          console.log("ok");
        }
      } else {
        console.log('write params')
      }
    },

  }
}


</script>

<style>
.workeritem{
  background-color: rgb(244, 244, 244);
  border: 10px;
  border-style:solid;
  border-color: rgb(226, 222, 215);
  padding: 40px;
  margin: 40px;
}

.text{color:black;}


button
{
  padding: 3px 6px;
  transition: 0.5s;
  background-color: white;
  border-radius: 4px;
  border: 1px solid black;
  width: 9em;

}
button:hover {
  background-color:  rgb(213, 202, 183);
  color: white;
  border: 1px solid rgb(149, 113, 52);
}

</style>

