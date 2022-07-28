<template>
  <div class="workeritem container uk-padding">
    <div class=" uk-card uk-card-default uk-card-body">
      <div>
        <div class="page-subtitle">
          <h4>Create department</h4>
        </div>

        <form @submit.prevent="createDepartment" enctype="multipart/form-data">

          <label for="pesel" class="uk-form-label">Name: </label>
          <input class="uk-input uk-form-controls" type="text" v-model="name" >

          <label for="imie" class="uk-form-label">Street: </label>
          <input class="uk-input uk-form-controls" type="text" v-model="street">

          <label for="nazwisko" class="uk-form-label">City: </label>
          <input class="uk-input uk-form-controls" type="text" v-model="city">

          <label for="age" class="uk-form-label">Postcode: </label>
          <input class="uk-input uk-form-controls" type="text" v-model="postcode">



          <button type="submit" class="uk-button uk-button-default uk-width-1-1@s">Add</button>
        </form>

      </div>

    </div>

  </div>

</template>

<script>
import axios from '@/lib/http-common'

// import {required} from 'vuelidate/lib/validators'


export default{
  name:'department-create',
  data() {
    return {
      name : "",
      street : "",
      city : "",
      postcode : "",



      errors: []
    }
  },

  methods: {
    async createDepartment() {
      if (this.postcode!= "" || this.name != "" || this.street != "") {
        this.errors = []
        const ob = {

          name: this.name,
          street: this.street,
          city: this.city,
          postcode: this.postcode,

        }
        await axios.post('/departments/add', ob, {
          headers: {
            'Content-Type': 'application/json'
          }

        });
      } else {
        this.errors.push("PESEL and/or name required")
      }

      this.$router.go();
    }

  }

}

</script>