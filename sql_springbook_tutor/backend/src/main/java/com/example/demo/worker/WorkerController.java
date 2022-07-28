package com.example.demo.worker;

import com.example.demo.child.Child;
import com.example.demo.salary.Salary;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@RequestMapping("/api/v1/users")
@RestController
public class WorkerController {

    private WorkerService workerService;

    @Autowired
    public WorkerController(WorkerService workerService) {
        this.workerService = workerService;
    }

    @DeleteMapping("/delete/{pesel}")
    void deleteByPesel(@PathVariable String pesel) {
        workerService.deleteByPesel(pesel);
    }

    @GetMapping("/all")
    List<Worker> getAll() {
        return workerService.findAllByOrderByPesel();
    }

    @GetMapping("/namelike/{name}")
    List<Worker> getByName(@PathVariable String name) {
        return workerService.findByImieOrNazwiskoContaining(name);
    }

    @GetMapping("/children/{pesel}")
    List<Child> getChildren(@PathVariable String pesel) {
        return workerService.getChildren(pesel);
    }

    @GetMapping("/salary/{pesel}")
    List<Salary> getSalary(@PathVariable String pesel) {
        return workerService.getSalary(pesel);
    }

    @GetMapping("/id/{pesel}")
    Worker getWorker(@PathVariable String pesel) {
        return workerService.findByPesel(pesel);
    }

    @GetMapping("/range/{limit}/{offset}")
    List<Worker> getWorkerInRange(@PathVariable int limit, @PathVariable int offset) {
        return workerService.findInRange(limit, offset);
    }

    @GetMapping("/department/{department}")
    List<Worker> getWorkerInDepartment(@PathVariable int department) {
        return workerService.findByDepartmentId(department);
    }

    @PostMapping("/users/add")
    void addWorker(@RequestBody Worker worker) {
        workerService.addWorker(worker);
    }

    @PostMapping("/salary/add/{pesel}")
    void addSalary(@PathVariable String pesel, @RequestBody Salary salary) {
        workerService.addSalary(pesel, salary);
    }

    @PutMapping("/children/add/{pesel}")
    void addChild(@PathVariable String pesel, @RequestBody Child child) {
        workerService.addChild(pesel, child);
    }

    @PutMapping("/update")
    void editWorker(@RequestBody Worker worker) {
        workerService.editWorker(worker);
    }

}
