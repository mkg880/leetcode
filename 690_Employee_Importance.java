/*
// Definition for Employee.
class Employee {
    public int id;
    public int importance;
    public List<Integer> subordinates;
};
*/

class Solution {
    public int getImportance(List<Employee> employees, int id) {
        Employee e = null;
        for(int i = 0; i < employees.size(); i++) {
            if(employees.get(i).id == id) {
                e = employees.get(i);
                break;
            }
        }
        int count = e.importance;
        for(int i : e.subordinates) {
            count += getImportance(employees, i);
        }
        return count;
    }
}