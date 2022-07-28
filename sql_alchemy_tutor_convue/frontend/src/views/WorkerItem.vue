<template>
  <div class="workeritem container uk-padding">
     <h1 class="uk-text-center">W O R K E R : {{this.worker.name}}  {{worker.surname}}</h1>

    <div class=" uk-card uk-card-default uk-card-body">

       <div id="contentW">

            <div id="Info">
              <table class="uk-table uk-table-responsive uk-table-divider">
                <thead>
                  <tr>
                    <th>
                      Main Info
                    </th>
                    <th>
                      Edit
                    </th>
                  </tr>
                </thead>
                <tbody>
                  <tr> <td>PESEL : &nbsp;{{ worker.pesel }}</td>
                 
                  <td>Name : &nbsp;{{ worker.name }}</td>
                  <td>Surname : &nbsp;{{ worker.surname }}</td>
                  <td>Criminal record : &nbsp;{{ worker.criminal_record }}</td>
                  <td>Department ID : &nbsp; <a @click="redirectToDeptProfile(worker.department_id)">{{ worker.department_id }}</a> </td>
                  <td> <button @click="redirectToWorkerEditForm" class="uk-button uk-button-default" type="button"><span uk-icon="icon:  triangle-down"></span>EDIT</button></td>
                  <td> <button @click="deleteWorker" class="uk-button uk-button-default" type="button"><span uk-icon="icon:  triangle-down"></span>DELETE</button></td>

                  
                  </tr>
        
                </tbody>
              </table>
                
            </div>
             <div>
                <br/>
                <br/>
                <h2>Salaries:</h2>

                <table class="uk-table uk-table-striped my-table">
                    <thead>
                        <tr>
                            <th>Month</th>
                            <th>Amount</th>

                        </tr>
                    </thead>
                    <tbody>

                        <tr v-for="salary in worker.owner_w" v-bind:key="salary.pesel">
                            <td>{{ salary.month }}</td>
                            <td>{{ salary.amount }}</td>
                        </tr>

                    </tbody>
                </table>
            </div>

            <div></div>

             <div>

                <h2>Childrens:</h2>

                <table class="uk-table uk-table-striped my-table">
                    <thead>
                        <tr>
                            <th>Name</th>
                            <th>DOB</th>

                        </tr>
                    </thead>
                    <tbody>

                        <tr v-for="(child) in worker.children" v-bind:key="child.name">
                            <td>{{ child.imie}}</td>
                            <td>{{child.dob.substr(0, 10)}}</td>
                        </tr>
                        

                    </tbody>
                </table>
            </div>
        </div>
    </div>

 </div>


</template>

<script>


import axios from '@/lib/http-common'
import Vue from 'vue'
import VueAxios from 'vue-axios'





Vue.use(VueAxios, axios)

export default {
  name:'workerItem',
  
  data() {
    return {
       worker: []

    }
  },
  mounted() {
    this.loadWorker()

  },
  methods: {
  async loadWorker() {
      const ret = await axios.get(`../workers/worker/${this.$route.params.pesel}`)
      this.worker = ret.data
    },
   redirectToDeptProfile(id) {
      this.$router.push({ path: `/departments/department/${id}` })
    },
     redirectToWorkerEditForm() {
      this.$router.push({ path: `../editworker/${this.$route.params.pesel}` })
    },

  // async deleteWorkerByPesel({ ...args }) {
  //       const params = {}
  //       if (args.pesel) params.pesel = args.pesel;
        
  //       if (params.pesel) {
  //           const searchParams = new URLSearchParams(params);
  //           const ret = await axios.delete(`/workers/delete/${searchParams.pesel}`, {})
  //           return ret.data;
  //       }        
  //       return {}
  //   },

    async deleteWorker(){
      console.log('in func')
      console.log(this.worker.pesel)
      await axios.delete(`/workers/delete/${this.worker.pesel}` ).then((resp) => {
                    this.worker = resp.data
                    
                })

                this.$router.push({ path: `../workers` });
               

      return {}

    }



  },

  computed:{
    destinationId() {
        return parseInt(this.$route.params.id)
    }

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