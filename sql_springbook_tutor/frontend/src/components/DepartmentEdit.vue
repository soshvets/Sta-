<template>
  <div>

    <p>Edit department</p>


    <div class="departmentitem uk-card-small uk-card-body  ">

      <form enctype="multipart/form-data" @submit.prevent="updateDepartment">
        <label for="first_name" class="uk-form-label">ID:  </label>
        <input class="uk-input uk-form-controls" type="number" v-model="ob.id">
        <label for="first_name" class="uk-form-label">Name: </label>
        <input class="uk-input uk-form-controls" type="text" v-model="ob.name">
        <label for="last_name" class="uk-form-label">Street: </label>
        <input class="uk-input uk-form-controls" type="text" v-model="ob.street">
        <label for="age" class="uk-form-label">City: </label>
        <input class="uk-input uk-form-controls" type="text" v-model="ob.city">
        <label for="age" class="uk-form-label">Postcode: </label>
        <input class="uk-input uk-form-controls" type="text" v-model="ob.postcode">

        <button type="submit" class="uk-button uk-button-default uk-width-1-1@s">Update</button>
      </form>

    </div>
  </div>

</template>

<script>
import axios from '@/lib/http-common'

export default{
  props: ['departments'],
  data() {
    return {

      ob: {}

    }
  },

  methods: {
    async updateDepartment() {
      console.log('in func')

      await axios.put('/departments/edit', this.ob, {
        headers: {
          'Content-Type': 'application/json'
        }

      });
    },
  }
}
</script>