<template>
  <div class="workeritem container uk-padding">
    <div class=" uk-card uk-card-default uk-card-body">
      <div>
        <div class="page-subtitle">
          <h4>Create worker</h4>
        </div>

        <form @submit="createWorker" enctype="multipart/form-data">

          <label for="pesel" class="uk-form-label">Pesel: </label>
          <input class="uk-input uk-form-controls" type="text" v-model="pesel" >

          <label for="imie" class="uk-form-label">First name: </label>
          <input class="uk-input uk-form-controls" type="text" v-model="name">

          <label for="nazwisko" class="uk-form-label">Last name: </label>
          <input class="uk-input uk-form-controls" type="text" v-model="surname">

          <label for="age" class="uk-form-label">Age: </label>
          <input class="uk-input uk-form-controls" type="number" v-model="age">

          <label for="department_id" class="uk-form-label">Department id: </label>
          <input class="uk-input uk-form-controls" type="number" v-model="department_id">

          <label for="criminal_record" class="uk-form-label">Criminal record: </label>
          <div uk-form-custom="target: > * > span:first-child" class="uk-form-controls">
            <select name="criminal_record" v-model="criminal_record">
              <option value="False">False</option>
              <option value="True">True</option>
            </select>
            <button class="uk-button uk-button-default" type="button" tabindex="-1">
              <span></span>
              <span uk-icon="icon: chevron-down"></span>
            </button>
          </div>

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
  name:'worker-create',
  data() {
    return {
      pesel: "",
      name: "",
      surname: "",
      age: "",
      department_id: 0,
      criminal_record: false,
      errors: []
    }
  },

  methods: {
    async createWorker() {
      if (this.pesel != "" || this.name != "" || this.surname != "") {
        this.errors = []
        const ob = {
          pesel: this.pesel,
          name: this.name,
          surname: this.surname,
          age: this.age,
          department_id: this.department_id,
          criminal_record: this.criminal_record
        }
        await axios.post('/workers/add', ob, {
          headers: {
            'Content-Type': 'application/json'
          }
        });
      } else {
        this.errors.push("PESEL and/or name required")
      }
    }
  }

}

</script>

<style lang="scss">
.input-field{
  padding: 1vh
}
#surname, #name {
  padding: 1vh;
  border-radius: 15px;
  border: 2px solid rgba(210, 50, 100, 0.502);
  background: linear-gradient(to left, rgba(253, 253, 251, 0.3), rgba(235, 212, 136, 0.3));
}


</style>