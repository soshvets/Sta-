package com.example.demo.department;
import com.example.demo.worker.Worker;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;

import java.util.List;

@Service
public class DepartmentService {

    private DepartmentRepository departmentRepo;

    @Autowired
    public DepartmentService(DepartmentRepository departmentRepo) {
        this.departmentRepo = departmentRepo;
    }

    public Department findById(int id) {
        return departmentRepo.findById(id);
    }

    public List<Department> findByNameContaining(String name) {
        return departmentRepo.findByNameContaining(name);
    }

    public List<Department> findByCityContaining(String city) {
        return departmentRepo.findByCityContaining(city);
    }

    public List<Department> findInRange(int limit, int offset) {
        return departmentRepo.findInRange(limit, offset);
    }

    public void addDepartment(Department department) {
        Department newDepartment = new Department();
        newDepartment = department;
        departmentRepo.save(newDepartment);
    }

    public void editDepartment(Department department) {
        Department departmentToUpdate = departmentRepo.findById(department.getId());
        departmentToUpdate = department;
        departmentRepo.save(departmentToUpdate);
    }

    public void deleteById(int id) {
        departmentRepo.deleteById(id);
    }

}
