using System;
using System.IO;
using System.Text;

namespace Project
{
    class Program
    {

        string[] record = new string[100];
        string[] customer_record = new string[100];
        string[] transaction_record = new string[100];

        int counter = 0;
        int customer_counter = 0;
        int active_counter_employe = 0;
        int customer_transaction_counter = 0;

        static void Main(string[] args)
        {
            int main_option = 0;
            Program call = new Program();
            while (main_option != 5)
            {
                call.main_menu();
                main_option = call.main_options();
                if (main_option == 1)
                {
                    call.main_menu();
                    call.employe_signin();
                }
                if (main_option == 2)
                {
                    call.main_menu();
                    call.customer_signin();
                }

                if (main_option == 3)
                {
                    call.main_menu();
                    call.customer_form();
                }

                if (main_option == 4)
                {
                    call.main_menu();
                    call.writeData();
                }


            }
        }

        //GET FIELD FUNTION
        string getfield(string field, int comma)
        {
            string temp = "";
            int counter = 0;
            int starting_counter;
            int coma_counter = 0;
            starting_counter = comma - 1;

            while (coma_counter != comma)
            {

                if (field[counter] == ',')
                {
                    coma_counter = coma_counter + 1;
                    counter = counter + 1;
                }

                if (starting_counter <= coma_counter && coma_counter != comma)
                {
                    temp = temp + field[counter];
                }

                counter = counter + 1;
            }

            return temp;
        }
        //




        void main_menu()
        {
            Console.Clear();
            Console.WriteLine("*************************************************************************");
            Console.WriteLine("*                          BANK MANAGEMENT SYSTEM                       *");
            Console.WriteLine("*************************************************************************");
        }

        int main_options()
        {
            int option;
            Console.WriteLine("MAIN MENU>>");
            Console.WriteLine("1.TO LOGIN AS A EMPLOYEE ");
            Console.WriteLine("2.TO LOGIN AS A CUSTOMER ");
            Console.WriteLine("3.OPEN YOUR ACCOUNT");
            Console.WriteLine("4.TO SAVE DATA INTO FILE");
            Console.WriteLine("5.EXIT");

            Console.Write("ENTER OPTION NUMBER =");
            option = int.Parse(Console.ReadLine());
            return option;
        }

        void employe_signin()
        {
            string employe_id;
            string password;
            string field;
            string category;
            Console.Write("ENTER YOUR EMPLOYE ID =");
            employe_id = Console.ReadLine();
            Console.Write("ENTER YOUR PASSWORD =");
            password = Console.ReadLine();

            if (employe_id == "MANAGER123" && password == "OK12")
            {
                int option = 0;
                while (option != 6)
                {
                    option = manager_menu();

                    if (option == 1)
                    {
                        main_menu();
                        readData();
                        add_employe();
                        writeData();


                    }
                    if (option == 2)
                    {
                        main_menu();
                        readData();
                        employe_experience();

                    }
                    if (option == 3)
                    {
                        main_menu();
                        readData();
                        view_employe();
                    }
                    if (option == 4)
                    {
                        main_menu();
                        string employe__id;
                        string name;
                        String status;
                        Console.Write("WRITE EMPLOYE ID =");
                        employe__id = Console.ReadLine();
                        Console.Write("ENTER EMPLOYE NAME =");
                        name = Console.ReadLine();
                        status = delete_employe_method(employe__id, name);
                        Console.WriteLine(status);
                        Console.ReadLine();
                        writeData();

                    }


                    if (option == 5)
                    {
                        main_menu();
                        string employe__id;
                        string name;
                        String status;
                        Console.Write("WRITE EMPLOYE ID =");
                        employe__id = Console.ReadLine();
                        Console.Write("ENTER EMPLOYE NAME =");
                        name = Console.ReadLine();
                        status = change_details(employe__id, name);
                        Console.WriteLine(status);
                        Console.ReadLine();
                        writeData();

                    }

                }
            }

            for (int x = 0; x < counter; x++)
            {
                field = record[x];
                category = getfield(field, 1);
                if (category == "employee")
                {
                    string employe_name;
                    string employe_id_check;
                    string employe_password;
                    string employe_experience;
                    employe_id_check = getfield(field, 2);
                    employe_name = getfield(field, 4);
                    employe_password = getfield(field, 3);
                    employe_experience = getfield(field, 5);
                    if (employe_id == employe_id_check && password == employe_password)
                    {
                        int option = 0;
                        active_counter_employe = x;
                        while (option != 6)
                        {
                            readData();
                            employe_menu(active_counter_employe);
                            Console.WriteLine("ENTER OPTION NO =");
                            option = int.Parse(Console.ReadLine());

                            if (option == 1)
                            {
                                main_menu();
                                accept_forms();
                                writeData();
                            }

                            if (option == 2)
                            {
                                main_menu();
                                customer_details();
                            }
                            if (option == 3)
                            {
                                main_menu();
                                customer_cash_deposit();
                                writeData();
                            }

                            if (option == 4)
                            {
                                main_menu();
                                customer_change_details();
                                writeData();
                            }
                            if (option == 4)
                            {
                                main_menu();
                                profit_calculation();
                            }
                        }
                        break;
                    }
                }
            }



        }


        //STRATS OF MANAGER OPTIONS METHODS
        int manager_menu()
        {

            main_menu();
            int option;
            Console.WriteLine("MAIN MENU>>MANAGER");
            Console.WriteLine("1.ADD EMPLOYE ");
            Console.WriteLine("2.EMPLOYE EXPERIENCE WISE");
            Console.WriteLine("3.VIEW EMPLOYEES");
            Console.WriteLine("4.DELETE EMPLOYEE");
            Console.WriteLine("5.CHANGE DETAILS");
            Console.WriteLine("6.LOGOUT");
            Console.WriteLine("ENTER OPTION NUMBER =");
            option = int.Parse(Console.ReadLine());
            return option;
        }
        void add_employe()
        {
            main_menu();
            string employe_id;
            string employe_password;
            string employe_name;
            string employe_experience;
            string temp;
            Console.Write("ENTER EMPLOYE ID =");
            employe_id = Console.ReadLine();
            Console.Write("ENTER EMPLOYE PASSWORD =");
            employe_password = Console.ReadLine();
            Console.Write("ENTER EMPLOYE NAME =");
            employe_name = Console.ReadLine();
            Console.Write("ENTER EMPLOYE EXPERIENCE =");
            employe_experience = Console.ReadLine();
            temp = "employee" + "," + employe_id + "," + employe_password + "," + employe_name + "," + employe_experience + ",";
            record[counter] = temp;
            Console.ReadKey();

            counter = counter + 1;
        }
        void view_employe()
        {
            main_menu();
            print_employe(counter);
            Console.ReadKey();
        }
        string delete_employe_method(string employe_id, string input_name)
        {
            string id;
            string field;
            string name;
            string status;
            string temp;

            for (int x = 0; x < counter; x++)
            {
                field = record[x];
                id = getfield(field, 2);
                name = getfield(field, 4);

                if (id == employe_id && input_name == name)
                {
                    for (int idx = x; x < counter; x++)
                    {
                        temp = record[idx + 1];
                        record[idx] = temp;
                    }
                    status = "EMPLOYE HAS BEMM DELEETED SUCESSULLY";
                    counter = counter - 1;
                    return status;
                }
            }
            status = "INFORMATION PROVIDED IS WRONG";
            return status;

        }
        string change_details(string employe_id, string input_name)
        {
            string id;
            string field;
            string name;
            string status;
            string employe_password;
            string employe_experience;
            string temp;

            for (int x = 0; x < counter; x++)
            {
                field = record[x];
                id = getfield(field, 2);
                name = getfield(field, 4);
                if (id == employe_id && name == input_name)
                {
                    employe_password = getfield(field, 3);
                    employe_experience = getfield(field, 5);
                    Console.WriteLine("1.TO CHANGE ID");
                    Console.WriteLine("2.TO CHANGE NAME");
                    Console.WriteLine("3.TO CHANGE PASSWORD");
                    Console.WriteLine("4.TO CHANGE EXPERIENCE");
                    int option;
                    Console.Write("ENTER OPTION NUMBER =");
                    option = int.Parse(Console.ReadLine());
                    if (option == 1)
                    {
                        Console.Write("ENTER NEW ID =");
                        id = Console.ReadLine();
                    }
                    if (option == 2)
                    {
                        Console.WriteLine("ENTER NEW NAME =");
                        name = Console.ReadLine();
                    }
                    if (option == 3)
                    {
                        Console.WriteLine("ENTER NEW PASSWORD =");
                        employe_password = Console.ReadLine();
                    }
                    if (option == 4)
                    {
                        Console.WriteLine("ENTER NEW EXPERIENCE =");
                        employe_experience = Console.ReadLine();
                    }
                    temp = "employee" + "," + id + "," + employe_password + "," + name + "," + employe_experience + ",";
                    record[x] = temp;
                    status = "INFORMATION HAS BEEN CHANGED SUCESSFULLY";
                    writeData();
                    return status;
                }
            }
            status = "INFORMATION PROVIDED IS WRONG";
            return status;

        }
        void employe_experience()
        {
            main_menu();
            int employe_experience;
            string field;
            int copy_counter = 0;
            int largest;
            copy_counter = counter;
            int swaping_index = 0;
            string temp = "";
            for (int x = 0; x < copy_counter; x++)
            {
                field = record[x];
                employe_experience = int.Parse(getfield(field, 5));
                largest = -100000;
                for (int y = 0; y < copy_counter; y++)
                {
                    if (largest < employe_experience)
                    {
                        largest = employe_experience;
                        temp = record[swaping_index];
                        record[swaping_index] = record[y];
                        record[y] = temp;
                    }
                }
                swaping_index = swaping_index + 1;
            }

            print_employe(copy_counter);
            Console.ReadKey();
        }
        void print_employe(int copy_counter)
        {
            Console.WriteLine("ID \t   PASSWORD\tNAME \t  EXPERIENCE");
            string field;
            string category;
            string employe_id;
            string employe_password;
            string employe_name;
            string employe_experience;
            for (int x = 0; x < counter; x++)
            {
                field = record[x];
                category = getfield(field, 1);

                if (category == "employee")
                {
                    employe_id = getfield(field, 2);
                    employe_password = getfield(field, 3);
                    employe_name = getfield(field, 4);
                    employe_experience = getfield(field, 5);
                    Console.WriteLine(employe_id + "\t   " + employe_password + "\t" + employe_name + "\t\t" + employe_experience);
                }
            }
        }

        // END OF MANAGER OPTIONS METHODS


        //START OF EMPLOYE OPTIONS
        void employe_menu(int active_counter)
        {
            main_menu();
            string employe_id;
            string field;
            field = record[active_counter];
            employe_id = getfield(field, 4);
            Console.WriteLine("MAIN MENUE >> EMPLOYE >>" + employe_id);
            Console.WriteLine("1.ACCEPT DETAILS");
            Console.WriteLine("2.CUSTOMER DETAILS");
            Console.WriteLine("3.CASH DEPOSIT");
            Console.WriteLine("4.CHANGE DETAILS");
            Console.WriteLine("5.PROFIT CALCULATION");
            Console.WriteLine("6.LOGOUT");
        }


        void accept_forms()
        {
            string first_name;
            string last_name;
            string cnic;
            string pinn;
            string account_no;
            string phone_number;
            string address;
            string field;
            string status;
            string category;
            string input;
            string temp;
            string cash = "0";
            for (int x = 0; x < customer_counter; x++)
            {
                field = customer_record[x];
                category = getfield(field, 1);
                if (category == "customer")
                {
                    first_name = getfield(field, 2);
                    last_name = getfield(field, 3);
                    cnic = getfield(field, 4);
                    pinn = getfield(field, 5);
                    account_no = getfield(field, 6);
                    phone_number = getfield(field, 7);
                    address = getfield(field, 8);
                    status = getfield(field, 9);
                    Console.WriteLine("NAME " + first_name + last_name + "\n" + "CNIC " + cnic + "\n" + "PINN  " + pinn + "\n" + "ACCOUNT NUMBER " + account_no + "\n" + "PHONE NUMBER " + phone_number + "\n" + "ADDRESS " + address + "\n" + "STATUS " + status);
                    input = Console.ReadLine();
                    if (input == "CANCEL")
                    {
                        break;
                    }
                    else if (input == "ACTIVE" || input == "INACTIVE")
                    {
                        status = input;
                        temp = "customer" + ',' + first_name + ',' + last_name + ',' + cnic + ',' + pinn + ',' + account_no + ',' + phone_number + ',' + address + ',' + status + ',' + cash + ',';
                        customer_record[x] = temp;
                    }
                    writeData();
                }
            }

        }

        void customer_details()
        {
            string account_number_input;
            string cnic;
            string cnic_input;
            string field;
            string category;
            string account_no;
            string first_name;
            string last_name;
            string pinn;
            string phone_number;
            string address;
            string status;

            Console.Write("ENTER CUSTOMER ACCOUNT NUMBER ");
            account_number_input = Console.ReadLine();
            Console.Write("ENTER CUSTOMER CNIC ");
            cnic_input = Console.ReadLine();
            for (int x = 0; x < customer_counter; x++)
            {
                field = customer_record[x];
                category = getfield(field, 1);
                cnic = getfield(field, 4);
                account_no = getfield(field, 6);


                if (category == "customer" && account_number_input == account_no && cnic == cnic_input)
                {
                    first_name = getfield(field, 2);
                    last_name = getfield(field, 3);
                    pinn = getfield(field, 5);
                    phone_number = getfield(field, 7);
                    address = getfield(field, 8);
                    status = getfield(field, 9);
                    Console.WriteLine("NAME " + first_name + last_name + "\n" + "CNIC " + cnic + "\n" + "PINN  " + pinn + "\n" + "ACCOUNT NUMBER " + account_no + "\n" + "PHONE NUMBER " + phone_number + "\n" + "ADDRESS " + address + "\n" + "STATUS " + status);
                    Console.WriteLine("PRESS ANY KEY TO CONTINUE..............");
                    Console.ReadLine();
                    break;
                }
            }
        }

        void customer_cash_deposit()
        {
            string account_number_input;
            string cnic;
            string cnic_input;
            string field;
            string category;
            string account_no;
            string first_name;
            string last_name;
            string pinn;
            string phone_number;
            string address;
            string status;
            int input;
            string temp;
            int cash;

            Console.Write("ENTER CUSTOMER ACCOUNT NUMBER ");
            account_number_input = Console.ReadLine();
            Console.Write("ENTER CUSTOMER CNIC ");
            cnic_input = Console.ReadLine();
            for (int x = 0; x < customer_counter; x++)
            {
                Console.WriteLine(x);
                field = customer_record[x];
                category = getfield(field, 1);
                cnic = getfield(field, 4);
                account_no = getfield(field, 6);
                Console.WriteLine(category);


                if (category == "customer" && account_number_input == account_no && cnic == cnic_input)
                {
                    first_name = getfield(field, 2);
                    last_name = getfield(field, 3);
                    pinn = getfield(field, 5);
                    phone_number = getfield(field, 7);
                    address = getfield(field, 8);
                    status = getfield(field, 9);
                    cash = int.Parse(getfield(field, 10));
                    Console.Write("ENTER AMMOUNT TO DEPOSIT");
                    input = int.Parse(Console.ReadLine());
                    if (input < 0)
                    {
                        Console.WriteLine("INVALID INPUT");

                    }
                    else
                    {
                        cash = cash + input;
                    }
                    temp = "customer" + ',' + first_name + ',' + last_name + ',' + cnic + ',' + pinn + ',' + account_no + ',' + phone_number + ',' + address + ',' + status + ',' + cash + ',';
                    Console.WriteLine(cash);
                    customer_record[x] = temp;
                    Console.WriteLine("PRESS ANY KEY TO CONTINUE..............");
                    Console.ReadLine();
                    writeData();
                    break;
                }
            }
        }

        void customer_change_details()
        {
            string account_number_input;
            string cnic;
            string cnic_input;
            string field;
            string category;
            string account_no;
            string first_name;
            string last_name;
            string pinn;
            string phone_number;
            string address;
            string status;
            int input;
            string temp = "";
            string cash;

            Console.Write("ENTER CUSTOMER ACCOUNT NUMBER ");
            account_number_input = Console.ReadLine();
            Console.Write("ENTER CUSTOMER CNIC ");
            cnic_input = Console.ReadLine();

            for (int x = 0; x < customer_counter; x++)
            {
                field = customer_record[x];
                category = getfield(field, 1);
                cnic = getfield(field, 4);
                account_no = getfield(field, 6);


                if (category == "customer" && account_number_input == account_no && cnic == cnic_input)
                {
                    first_name = getfield(field, 2);
                    last_name = getfield(field, 3);
                    pinn = getfield(field, 5);
                    phone_number = getfield(field, 7);
                    address = getfield(field, 8);
                    status = getfield(field, 9);
                    cash = getfield(field, 10);
                    input = int.Parse(Console.ReadLine());

                    Console.WriteLine("1.TO CHANGE FIRST NAME");
                    Console.WriteLine("2.TO CHANGE LAST NAME");
                    Console.WriteLine("3.TO CHANGE PINN");
                    Console.WriteLine("4.TO CHANGE PHONE NUMBER ");
                    Console.WriteLine("5.TO CHANGE ADDRESS");
                    temp = "customer" + ',' + first_name + ',' + last_name + ',' + cnic + ',' + pinn + ',' + account_no + ',' + phone_number + ',' + address + ',' + status + ',' + cash + ',';

                    if (input == 1)
                    {
                        string new_first_name;
                        Console.Write("ENTER NEW FIRST NAME =");
                        new_first_name = Console.ReadLine();
                        temp = "customer" + ',' + new_first_name + ',' + last_name + ',' + cnic + ',' + pinn + ',' + account_no + ',' + phone_number + ',' + address + ',' + status + ',' + cash + ',';
                    }


                    if (input == 2)
                    {
                        string new_last_name;
                        Console.Write("ENTER NEW LAST NAME =");
                        new_last_name = Console.ReadLine();
                        temp = "customer" + ',' + first_name + ',' + new_last_name + ',' + cnic + ',' + pinn + ',' + account_no + ',' + phone_number + ',' + address + ',' + status + ',' + cash + ',';
                    }

                    if (input == 3)
                    {
                        string new_pinn;
                        Console.Write("ENTER NEW PINN =");
                        new_pinn = Console.ReadLine();
                        temp = "customer" + ',' + first_name + ',' + last_name + ',' + cnic + ',' + new_pinn + ',' + account_no + ',' + phone_number + ',' + address + ',' + status + ',' + cash + ',';
                    }

                    if (input == 4)
                    {
                        string new_phonenumber;
                        Console.Write("ENTER NEW PHONE NUMBER =");
                        new_phonenumber = Console.ReadLine();
                        temp = "customer" + ',' + first_name + ',' + last_name + ',' + cnic + ',' + pinn + ',' + account_no + ',' + new_phonenumber + ',' + address + ',' + status + ',' + cash + ',';
                    }

                    if (input == 5)
                    {
                        string new_address;
                        Console.Write("ENTER NEW ADRESS =");
                        new_address = Console.ReadLine();
                        temp = "customer" + ',' + first_name + ',' + last_name + ',' + cnic + ',' + pinn + ',' + account_no + ',' + phone_number + ',' + new_address + ',' + status + ',' + cash + ',';
                    }

                    customer_record[x] = temp;
                    writeData();
                    break;
                }
            }
        }

        void profit_calculation()
        {
            float ammount;
            int year;
            float calculation;
            Console.Write("ENTER AMMOUNT TO CALCULATE = ");
            ammount = float.Parse(Console.ReadLine());
            Console.Write("ENTER NUMBER  OF YEARS = ");
            year = int.Parse(Console.ReadLine());
            calculation = ammount * year / 100;
            Console.WriteLine("PRFIT ON THIS AMMOUNT IS =" + calculation);
            Console.ReadLine();


        }
        //END OF EMPLOYE OPTION



        //STARTING OF CUSTOMER OPTIONS
        void customer_signin()
        {
            main_menu();
            string account_no;
            string pinn;
            string comparing_account_no;
            string comparing_pinn;
            string field;
            string status;
            Console.Write("ENTER YOUR ACCOUNT NO=");
            account_no = Console.ReadLine();
            Console.Write("ENTER YOUR PINN=");
            pinn = Console.ReadLine();
            for (int x = 0; x < customer_counter; x++)
            {
                field = customer_record[x];
                comparing_account_no = getfield(field, 6);
                comparing_pinn = getfield(field, 5);
                if (comparing_account_no == account_no && comparing_pinn == pinn)
                {
                    status = getfield(field, 9);
                    if (status == "ACTIVE")
                    {
                        int option = 0;
                        while (option != 5)
                        {
                            readData();
                            customer_menue(x);
                            option = int.Parse(Console.ReadLine());
                            if (option == 1)
                            {
                                main_menu();
                                customer_account_deatils(x);
                            }

                            if (option == 2)
                            {
                                main_menu();
                                customer_account_balance(x);
                            }

                            if (option == 3)
                            {
                                main_menu();
                                customer_paybill(x);
                            }

                            if (option == 4)
                            {
                                main_menu();

                            }
                        }

                    }
                    else
                    {
                        main_menu();
                        Console.WriteLine("YOUR ACCOUNT IS NOT ACTIVE WAIT UNTLLS OUR EMPLOYE ACTIVE YOUR STATUS");
                        Console.WriteLine("PRESS ANY KEY TO CONTINUE");
                        Console.ReadLine();
                    }
                    break;

                }

            }
        }
        void customer_menue(int idx)
        {
            string comparing_account_no;
            string field;
            field = customer_record[idx];
            comparing_account_no = getfield(field, 6);
            main_menu();
            Console.WriteLine("MAIN MENUE >> CUSTOMER >>ACCOUNT NUMBER >>  " + comparing_account_no);
            Console.WriteLine("1.TO SEE ACCOUNT DETAILS ");
            Console.WriteLine("2.TO SEE ACCOUNT BALANCE  ");
            Console.WriteLine("3.PAY BILL ");
            Console.WriteLine("4.TRANSACTION DETAILS");
            Console.WriteLine("5.LOGOUT");
            Console.Write("ENTER ANY OPTION =");
        }

        void customer_account_deatils(int idx)
        {
            string first_name;
            string last_name;
            string pinn;
            string phone_number;
            string address;
            string status;
            string field;
            string account_number;
            string cnic;

            field = customer_record[idx];
            first_name = getfield(field, 2);
            last_name = getfield(field, 3);
            pinn = getfield(field, 5);
            account_number = getfield(field, 6);
            phone_number = getfield(field, 7);
            address = getfield(field, 8);
            cnic = getfield(field, 4);
            status = getfield(field, 9);
            main_menu();
            Console.WriteLine("NAME  " + first_name + " " + last_name + "\n" + "ACCOUNT NUMBER  " + account_number + "\n" + "CNIC " + cnic + "PINN " + pinn + "\n" + "PHONE NUMBER " + phone_number + "\n" + "ADDRESS " + address + "\n" + "STATUS " + status);
            Console.WriteLine("PRESS ANY KEY TO CONTINUE =");
            Console.ReadLine();
        }

        void customer_account_balance(int idx)
        {
            string field;
            string cash;
            field = customer_record[idx];
            cash = getfield(field, 10);
            Console.WriteLine(" YOUR ACCOUNT BALANCE IS RUPESS =" + cash);
            Console.WriteLine("PRESS ANY KEY TO CONTINUE ......................");
            Console.ReadLine();
        }


        void customer_paybill(int idx)
        {
            string bill_type;
            string bill_id;
            int ammount;
            int caparing_ammount;
            string field;
            string first_name;
            string last_name;
            string cnic;
            string pinn;
            string account_no;
            string phone_number;
            string address;
            string status;
            string temp;
            string change;
            string transaction;
            field = customer_record[idx];

            first_name = getfield(field, 2);
            last_name = getfield(field, 3);
            cnic = getfield(field, 4);
            pinn = getfield(field, 5);
            account_no = getfield(field, 6);
            phone_number = getfield(field, 7);
            address = getfield(field, 8);
            status = getfield(field, 9);

            Console.Write("ENTER BILL TYPE =");
            bill_type = Console.ReadLine();
            Console.Write("ENTER BILL ID   =");
            bill_id = Console.ReadLine();
            Console.WriteLine("ENTER AMMOUNT TO PAY  =");
            ammount = int.Parse(Console.ReadLine());
            if (ammount > 0)
            {
                caparing_ammount = int.Parse(getfield(field, 10));
                if (caparing_ammount >= ammount)
                {
                    caparing_ammount = caparing_ammount - ammount;
                    change = caparing_ammount.ToString();
                    Console.WriteLine("TRANSACTION HAS BEEN DONED");
                    temp = "customer" + ',' + first_name + ',' + last_name + ',' + cnic + ',' + pinn + ',' + account_no + ',' + phone_number + ',' + address + ',' + status + ',' + change + ',';
                    customer_record[idx] = temp;
                    transaction = "transaction" + ',' + account_no + ',' + bill_type + ',' + bill_id + ',' + ammount + ",";
                    transaction_record[customer_transaction_counter] = transaction;
                    customer_transaction_counter = customer_transaction_counter + 1;
                    writeData();
                    readData();
                }
                else
                {
                    Console.WriteLine("TRANSACTION FALED \n ACCOUNT BALANCE IS LOW");
                    Console.ReadLine();

                }
            }
            else
            {
                Console.WriteLine("TRANSACTION FALED \n INVALID AMMOUNT");
                Console.ReadLine();

            }


        }


        void customer_transaction(string account_number)
        {
            string account;
            string bill_id;
            string bill_type;
            string field;
            string ammount;
            for (int x = 0; x < customer_transaction_counter; x++)
            {
                field = transaction_record[x];
                bill_id = getfield(field, 4);
                bill_type = getfield(field, 3);
                account = getfield(field, 2);
                ammount = getfield(field, 5);
                if (account == account_number)
                {
                    Console.WriteLine("ACCOUNT NUMBER =" + account + "\n" + "AMMOUNT " + ammount + "\n" + "BILL ID" + bill_id + "BILL TYPE" + bill_type);
                    Console.WriteLine("PRESS ANY KET TO CONTINUE .........");
                    Console.ReadLine();
                }
            }
        }

        //CUSTOMER REGISTRATION FORM
        void customer_form()
        {
            main_menu();
            int min = 273649;
            int max = 432593;
            Console.WriteLine("FILL THE REQUIRED INFORMATION STEP BY STEP");
            string first_name;
            string last_name;
            string cnic;
            string pinn;
            string account_no;
            string phone_number;
            string address;
            string status;
            string temp;
            string cash = "0";
            Console.Write("ENTER YOUR FIRST NAME =");
            first_name = Console.ReadLine();
            Console.Write("ENTER YOUR LAST NAME =");
            last_name = Console.ReadLine();
            Console.Write("ENTER YOUR CNIC =");
            cnic = Console.ReadLine();
            Console.Write("ENTER YOUR PINN =");
            pinn = Console.ReadLine();
            Console.Write("ENTER YOUR PHONE NUMBER =");
            phone_number = Console.ReadLine();
            Console.Write("ENTER YOUR ADDRESS =");
            address = Console.ReadLine();
            Random random = new Random();
            int number = random.Next(min, max);
            account_no = Convert.ToString(number);
            status = "IN-ACTIVE";
            temp = "customer" + ',' + first_name + ',' + last_name + ',' + cnic + ',' + pinn + ',' + account_no + ',' + phone_number + ',' + address + ',' + status + ',' + cash + ',';
            customer_record[customer_counter] = temp;
            Console.WriteLine();
            Console.WriteLine(" YOUR ACCOUNT NUMBER IS =" + account_no);
            Console.WriteLine(" YOUR INFORMATION IS COLLECTED SUCESSFULLY");
            Console.WriteLine(" YOU CAN LOGIN TO YOUR ACCOUNT AS SOON AS OUR EMPLOYEE ACCEPTS YOUR FORM");
            Console.WriteLine(" THANK YOU FOR CHOSING LIFE LINE BANK ");
            Console.ReadLine();
            customer_counter = customer_counter + 1;
            writeData();
        }
        //END OF CUSTOMER OPTIONS    

        //FILE READING FUNTION  STARTS

        void writeData()
        {
            string data = "";
            FileStream fs = new FileStream("E:\\C#\\WEEK-6\\RECORD.txt", FileMode.Create, FileAccess.Write);
            StreamWriter sw = new StreamWriter(fs);
            for (int x = 0; x < customer_counter; x++)
            {
                data = customer_record[x];
                sw.WriteLine(data);
            }
            for (int x = 0; x < counter; x++)
            {
                data = record[x];
                sw.WriteLine(data);
            }

            sw.Flush();
            sw.Close();
            fs.Close();


        }

        void readData()
        {
            string[] temp = new string[100];
            int temp_counter = 0;
            FileStream fs = new FileStream("E:\\C#\\WEEK-6\\RECORD.txt", FileMode.Open, FileAccess.Read);
            StreamReader sr = new StreamReader(fs);
            sr.BaseStream.Seek(0, SeekOrigin.Begin);
            string str = "";
            while (str != null)
            {
                str = sr.ReadLine();
                temp[temp_counter] = str;
                temp_counter = temp_counter + 1;
            }
            sr.Close();
            fs.Close();

            string category = "";
            string temporary = "";
            temp_counter = temp_counter - 1;
            counter = 0;
            customer_counter = 0;
            customer_transaction_counter = 0;

            for (int x = 0; x < temp_counter; x++)
            {
                temporary = temp[x];
                category = getfield(temporary, 1);
                Console.WriteLine(temporary);
                if (category == "employee")
                {
                    record[counter] = temp[x];
                    counter = counter + 1;
                }

                else if (category == "customer")
                {
                    customer_record[customer_counter] = temporary;
                    customer_counter = customer_counter + 1;
                }

                else if (category == "transaction")
                {
                    transaction_record[customer_transaction_counter] = temporary;
                    customer_transaction_counter = customer_transaction_counter + 1;
                }


            }
        }


        //END



    }
}
