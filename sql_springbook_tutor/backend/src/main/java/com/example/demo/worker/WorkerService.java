package com.example.demo.worker;
import com.example.demo.child.Child;
import com.example.demo.department.DepartmentRepository;
import com.example.demo.salary.Salary;
import com.example.demo.salary.SalaryRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;

import java.util.ArrayList;
import java.util.List;
@Service
public class WorkerService {

    private WorkerRepository workerRepo;
    private DepartmentRepository departmentRepo;
    private SalaryRepository salaryRepo;


    @Autowired
    public WorkerService(WorkerRepository workerRepo, DepartmentRepository departmentRepo,
                         SalaryRepository salaryRepo) {
        this.workerRepo = workerRepo;
        this.departmentRepo = departmentRepo;
        this.salaryRepo = salaryRepo;
    }

    @Transactional
    public void deleteByPesel(String pesel) {
        workerRepo.deleteByPesel(pesel);
    }


    public List<Worker> findAllByOrderByPesel() {
        return workerRepo.findAllByOrderByPesel();

    }

    public List<Worker> findByImieOrNazwiskoContaining(String name) {
        return workerRepo.findByImieOrNazwiskoContaining(name);
    }

    public List<Child> getChildren(String pesel) {
        return workerRepo.findByPesel(pesel).getChildren();
    }

    public List<Salary> getSalary(String pesel) {
        return workerRepo.findByPesel(pesel).getSalary();
    }

    public Worker findByPesel(String pesel) {
        return workerRepo.findByPesel(pesel);
    }

    public List<Worker> findInRange(int limit, int offset) {
        return workerRepo.findInRange(limit, offset);
    }

    public List<Worker> findByDepartmentId(int department) {
        return workerRepo.findByDepartmentId(department);
    }

    public void addWorker(Worker worker) {
        Worker newWorker = new Worker();
        newWorker.setPesel(worker.getPesel());
        newWorker.setImie(worker.getImie());
        newWorker.setNazwisko(worker.getNazwisko());
        newWorker.setAge(worker.getAge());
        newWorker.setCriminal_record(worker.isCriminal_record());
        newWorker.setDepartment(departmentRepo.findById(worker.getDepartment_id()));
        workerRepo.save(newWorker);
    }

    public void addSalary(String pesel, Salary salary) {
        Salary newSalary = new Salary();
        newSalary.setWorkerPesel(pesel);
        newSalary.setAmount(salary.getAmount());
        newSalary.setMonth(salary.getMonth());
        salaryRepo.save(newSalary);

    }

    public void addChild(String pesel, Child child) {
        List<Child> childrenList = new ArrayList<>();
        Worker worker = workerRepo.findByPesel(pesel);
        childrenList = worker.getChildren();
        if (childrenList == null) {
            childrenList = new ArrayList<>();
        }
        childrenList.add(child);
        worker.setChildren(childrenList);
        workerRepo.save(worker);

    }

    public void editWorker(Worker worker) {
        Worker workerToUpdate = workerRepo.findByPesel(worker.getPesel());
        workerToUpdate.setImie(worker.getImie());
        workerToUpdate.setNazwisko(worker.getNazwisko());
        workerToUpdate.setAge(worker.getAge());
        workerToUpdate.setCriminal_record(worker.isCriminal_record());
        workerToUpdate.setDepartment(departmentRepo.findById(worker.getDepartment_id()));
        workerRepo.save(workerToUpdate);

    }

}
