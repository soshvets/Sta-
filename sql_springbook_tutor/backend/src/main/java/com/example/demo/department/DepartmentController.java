package com.example.demo.department;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@RestController
@RequestMapping(path = "api/v1/department")
public class DepartmentController {

    private DepartmentService departmentService;

    @Autowired
    public DepartmentController(DepartmentService departmentService) {
        this.departmentService = departmentService;
    }

    @GetMapping("/id/{id}")
    public Department getDepartment(@PathVariable int id) {
        return departmentService.findById(id);}

    @GetMapping("/name/{name}")
    public List<Department> getDepartmentByName(@PathVariable String  name){
        return departmentService.findByNameContaining(name);
    }

    @GetMapping("/city/{city}")
    public List<Department> getDepartmentByCity(@PathVariable String city){
        return departmentService.findByCityContaining(city);
    }


    @GetMapping("/range/{limit}/{offset}")
    public List<Department> getDepartmentInRange(@PathVariable int limit, @PathVariable int offset){
        return departmentService.findInRange(limit, offset);
    }

    @PostMapping("/add")
    public void addDepartment(Department department) {departmentService.addDepartment(department);}

    @PutMapping("/edit")
    public void editDepartment(Department department){
        departmentService.editDepartment(department);
    }

    @DeleteMapping("delete/{id}")
    public void deleteDepartmentById(@PathVariable int id){ departmentService.deleteById(id);}





}
