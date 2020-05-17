package behavioral.visitor;

import java.util.ArrayList;
import java.util.List;

import java.util.List;
import java.util.ArrayList;

public class CustomerGroup {
    private List<Customer> customers = new ArrayList<>();

    void accept(Visitor visitor) {
        for (Customer customer : customers) {
            customer.accept(visitor);
        }
    }

    void addCustomer(Customer customer) {
        customers.add(customer);
    }
}
