<template>
  <div class="container uk-padding  ">
    <h1 class="uk-text-center">W O R K E R S</h1>

    <div class="interractive-form uk-child-width-1-2 uk-text-center" uk-grid>
      

      <div class="uk-card uk-card-default uk-card-body">
        <label>If you want to create new employee, click   -   </label>
        <span></span>
            <button @click="redirectToWorkerCreateForm" class="uk-button uk-button-default" type="button"><span uk-icon="icon:  triangle-down"></span>Create</button>
             <div uk-dropdown="mode: click; boundary: ! .uk-button-group; boundary-align: true;">
               <ul class="uk-nav uk-dropdown-nav">
               </ul>
             </div>
      </div>
         <div class="uk-card uk-card-default uk-card-body">   
           <label> Find an employee you need  </label>    
           <div>
              <input v-model="name" @keyup.enter="loadList" />                                           
              <button @click="loadList" class="uk-button uk-button-default" type="button">Search</button> 
           </div>  
      </div>
     </div>
  
    <div>
        <table class="workers uk-table uk-table-responsive uk-table-divider">
          <thead>
              <tr>
                <th>PESEL</th>
                <th>Name</th>
                <th>Surname</th>
                <th></th>
                <th>Department_id</th>
              </tr>
          </thead>
          <tbody>
              <tr v-for="(worker) in items" v-bind:key="worker.pesel">   
                 <td class="uk-link-reset"><a @click="redirectToWorkerProfile(worker.pesel)">{{ worker.pesel }}</a></td>
                <td>{{worker.name}}</td>
                <td>{{worker.surname}}</td>
                <td>

            <div v-for="child in worker.children" v-bind:key="child.imie" v-show="worker.showChildren">
              <br />
              <span>Name: {{ child.imie }}</span><br />
              <span>dob: {{ child.dob }}</span><br />
              <span></span>

            </div>
          </td>
          <td class="uk-link-reset"><a @click="redirectToDeptProfile(worker.department_id)">{{ worker.department_id }}</a></td>
          </tr>    
          </tbody>
        </table>
      </div>
      <Paginate-cons
                :v-model="page"
                :page-count="pageCount"
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



export default{
  name: 'workers-view',
  
mixins: [paginationMixin],
data() {
    return {
        List: [],
        data: null,
        name:""
      }
  },

  mounted() {
   
  },
  methods:{
  async loadList() {
      const ret = await axios.get(`/workers/${this.name}`) 
       for (let i = 0; i < this.List.length; i++) {
            this.List[i].showChildren = false;
          }

      this.List = ret.data
      this.setupPagination(this.List)
    },

     redirectToDeptProfile(id) {
      this.$router.push({ path: `departments/department/${id}` })
    },
     redirectToWorkerProfile(pesel) {
      this.$router.push({ path: `../workerprofile/${pesel}` })
    },
     redirectToWorkerCreateForm() {
      this.$router.push({ path: `../createworker` })
    }


  },
  

}

</script>



<style>

.interractive-form{
  padding: 1fr;
  margin: 2fr;
}

h1{
  margin-bottom: 2fr;
  padding: 3%;
  background-color: rgb(226, 222, 215, 0.3);
  border: 10px;
  border-style:solid;
  border-color: rgb(226, 222, 215);
}

.uk-link-reset{
 font-weight: bold;

}

label {
  margin: 2fr;
  padding: 1fr;
  background-color: hsl(34, 78%, 91%, 0.45);
  font-family:'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
}

button {

  font-family:'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
}

.workers
{
  grid-column-start: 5;
  grid-column-end: 7;
  grid-row-start: 1;
  grid-row-end: 3;
  align-self: stretch;
  text-align: left;
  background-color: rgb(244, 244, 244);
  border: 10px;
  border-style:solid;
  border-color: rgb(226, 222, 215);
  padding: 40px;
  margin-top: 40px;

  
}

</style>
