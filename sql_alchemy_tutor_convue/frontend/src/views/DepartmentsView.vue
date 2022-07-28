<template>
  <div class=" departments container uk-padding">
         <input v-model="deptName" @keyup.enter="loadList" />                                           
              <button @click="loadList" class="uk-button uk-button-default" type="button">Search</button> 

                <button @click="redirectToDepartmentCreateForm" class="uk-button uk-button-default" type="button"><span uk-icon="icon:  triangle-down"></span>Create</button>

    <h1>Departments</h1>
     <div>
        <table class="table-class uk-table uk-table-responsive uk-table-divider">
          <thead>
              <tr>
                <th>ID</th>
                <th>Name</th>
                <th>Street</th>
             
              </tr>
          </thead>
          <tbody>
              <tr v-for="department in items" v-bind:key="department.id"> 
                <td>
                  {{department.id}}
                  <!-- <router-link :to="{ name: 'department', params: { id: department.id }}">{{department.id}}</router-link> -->
                </td>
                <!--  -->
                <td>{{department.name}}</td>
                <td>{{department.street}}</td>
                <button class="uk-button uk-button-default"  @click="departmentInfo(department.id)">Department Info</button> 
                <button class="uk-button uk-button-default"  @click="deleteDepartment(department.id)">Delete department</button>
                 <button @click="redirectToDepartmentEditForm" class="uk-button uk-button-default" type="button"><span uk-icon="icon:  triangle-down"></span>Edit</button>
                 <!-- <router-link :to="{ name: 'department', params: { id: department.id }}">{{department.id}}</router-link> -->
  
      
              </tr>
          </tbody>
        </table>
      </div>
        <Paginate-cons :page-count="pageCount"
                :click-handler="pageChangeHandler"
                :prev-text="'Prev'"
                :next-text="'Next'"
                :container-class="'uk-pagination uk-flex-center'"
                :page-class="'uk-active'"/>
  </div>
</template>


<script>

import axios from '@/lib/http-common'

import Vue from 'vue'
import VueAxios from 'vue-axios'
import paginationMixin from '@/mixins/pagination.mixin.js'


Vue.use(VueAxios, axios)

export default {
  mixins: [paginationMixin],
  data() {
      return {
          List: [],
          data: null,
          deptName:""

        }
  },
  methods:{
  async loadList() {
      const ret = await axios.get(`/departments/all/${this.deptName}`) 
      this.List = ret.data
      this.setupPagination(this.List)
    },

  async deleteDepartment(id){
   console.log(id)
    await axios.delete(`/departments/${id}`).then((resp) => {id = resp.data})
    console.log('del')
    this.$router.go(); //odswieża strone

  },
   departmentInfo(id) {
      this.$router.push({ path: `departments/department/${id}` })
    },
      redirectToDepartmentCreateForm() {
      this.$router.push({ path: `../createdepartment` })
    },
  
    redirectToDepartmentEditForm() {
      this.$router.push({ path: `../editdepartment` })
    },
      

  }

}

</script>

<style>
.deparments
{
  background-color: rgb(251, 208, 143);
  grid-column-start: 5;
  grid-column-end: 7;
  grid-row-start: 1;
  grid-row-end: 3;
  align-self: stretch;
  text-align: left;
  
}

.table-class{
  background-color: rgb(244, 244, 244);
  border: 10px;
  border-style:solid;
  border-color: rgb(226, 222, 215);
}

h1{
  text-align: center;
}

input{
        padding: 2px;
        margin-left: 30px;
        margin-right: 5px;

    }
    
    input:active{
        border: 1px solid black;
    }

button {

  font-family:'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
}



</style>
