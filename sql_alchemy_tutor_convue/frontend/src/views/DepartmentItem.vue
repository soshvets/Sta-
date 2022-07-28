<template>
  <div class="departmentitem container uk-padding">
    <div class=" uk-card uk-card-default uk-card-body">
      <table class="table-class uk-table uk-table-responsive uk-table-divider">
        <thead>
              <tr>
                <th>ID</th>
                <th>Name</th>
                <th>Street</th>
                <th>City</th>
                <th>Postcode</th>
              </tr>
          </thead>
          <tbody>
            <td>      {{ department.id }}      </td>
            <td>      {{ department.name }}      </td>
            <td>      {{ department.street }}      </td>
            <td>     {{ department.city }}       </td>
            <td>      {{ department.postcode }}      </td>

          </tbody>
      </table>
        <button v-on:click="showWorkers(department.index)">
        <span v-if="department.showWorkers">hide workers</span>
        <span v-else>show workers</span>
        </button>
        
        <div v-for="worker in department.workers" v-bind:key="worker.pesel" v-show="department.showWorkers">
        <br/>
        <span>Pesel: <a @click="redirectToWorkerProfile(worker.pesel)">{{ worker.pesel }}</a></span><br/>
        <span>Name: {{worker.name}}</span><br/>
        <span>Last Name: {{worker.surname}}</span><br/>
        <span>Age: {{worker.age}}</span><br/>
        <button @click="deleteWorkerFromDepartment(worker.pesel, department.id)">Delete worker from department</button>
        <span></span>
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
  data() {
    return {
      department: [],
      data: null,
      loading: true,
      department_id: 0
    }
  },
  mounted() {
    this.loadInfo();
    this.showWorkers();

  },
  methods: {
    async loadInfo() {
      const ret = await axios.get(`/departments/department/${this.$route.params.id}`)
      console.log(ret)
      this.department = ret.data
      for(let i=0; i < this.department.length;i++)
        {
          this.department[i].showWorkers = false;
  
        }
    },
    //TODO: Worker.dep.id = 0;
    async deleteWorkerFromDepartment(worker_pesel, department_id){
      console.log('in func')
      console.log(worker_pesel)
      
     console.log(department_id)
   
      await axios.put(`/departments/department/${department_id}/${worker_pesel}`, {}, { headers: { 'Content-Type': 'application/json' } }).then((resp) => {worker_pesel = resp.data});
      this.$router.go();
  


    },
    showWorkers()
      {
          this.department.showWorkers = !this.department.showWorkers;
          this.$forceUpdate();
      },

    
      
     redirectToWorkerProfile(pesel) {
      this.$router.push({ path: `/workerprofile/${pesel}` })
    }
  }

}

</script>


<style>
.departmentitem{
    background-color: rgb(244, 244, 244);
  border: 10px;
  border-style:solid;
  border-color: rgb(226, 222, 215);
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