using System;
using System.Collections;


namespace Mail_system
{

    class User
    {
        private string userName = "";
        private string password = "";
        private string user_category = "";
        public User(string username, string password)
        {
            this.userName = username;
            this.password = password;
        }

        public string get_username()
        {
            return this.userName;
        }


        public string get_password()
        {
            return this.password;
        }

        public bool set_user_category(string category)
        {
            if (category == "USER" || category == "ADMIN")
            {
                this.user_category = category;
                return true;
            }
            return false;
        }

        public string get_user_category()
        {
            return this.user_category;
        }


    }

    class UserCrud
    {
        private ArrayList allUsers = new ArrayList();
        private UserCrud()
        { }
        static UserCrud usercrud;
        public static UserCrud object_existance()
        {
            if (usercrud == null)
            {
                usercrud = new UserCrud();
            }
            return usercrud;
        }


        public string add_users(string username, string password, String category)
        {
            bool condition_category = false;
            User user_Object = new User(username, password);
            condition_category = user_Object.set_user_category(category);
            if (condition_category == true)
            {
                allUsers.Add(user_Object);
                return "USER ADDED SUCESSFULLY";
            }

            return "INVALID CATEGORY";

        }

        public string newAdmin_security(string pinn)
        {
            if (pinn == "ADMINOK1234")
            {
                return "VALID";
            }
            return "IN-VALID";

        }
        public string user_verification(string username, string password)
        {
            if (password == "RECIEVER_VERIFICATION")
            {
                for (int x = 0; x < allUsers.Count; x++)
                {
                    User temp = (User)allUsers[x];
                    if (temp.get_username() == username)
                    {
                        if (temp.get_user_category() == "ADMIN")
                        {
                            return "ADMIN";
                        }
                        else if (temp.get_user_category() == "USER")
                        {
                            return "USER";
                        }
                    }
                }
            }
            else
            {
                for (int x = 0; x < allUsers.Count; x++)
                {
                    User temp = (User)allUsers[x];
                    if (temp.get_username() == username && temp.get_password() == password)
                    {
                        if (temp.get_user_category() == "ADMIN")
                        {
                            return "ADMIN";
                        }
                        else if (temp.get_user_category() == "USER")
                        {
                            return temp.get_username();
                        }
                    }
                }
            }
            return "USER NOT FOUND";
        }

        public ArrayList viewAll_users()
        {
            ArrayList all_users = new ArrayList();
            for (int x = 0; x < allUsers.Count; x++)
            {
                User temp = (User)allUsers[x];
                if (temp.get_user_category() == "USER")
                {
                    all_users.Add(allUsers[x]);
                }
            }
            return all_users;
        }

        public String update_pinn(string username, string pinn)
        {
            for (int x = 0; x < allUsers.Count; x++)
            {
                User temp = (User)allUsers[x];
                if (temp.get_user_category() == "USER" && temp.get_username() == username)
                {
                    User user_Object = new User(username, pinn);
                    user_Object.set_user_category("USER");
                    allUsers[x] = user_Object;
                    return "PINN HAS BEEN UPDATED";

                }
            }
            return "INVALID USER";
        }
    }


    class Messages
    {
        private string messages;
        private string sender_name;
        private string reciever_name;

        public Messages(string messages)
        {
            this.messages = messages;
        }
        public void set_receiver(string reciever_name)
        {
            this.reciever_name = reciever_name;
        }

        public void set_sender(string sender_name)
        {
            this.sender_name = sender_name;
        }

        public string get_receiver()
        {
            return this.reciever_name;
        }

        public string get_sender()
        {
            return this.sender_name;
        }

        public string get_message()
        {
            return this.messages;
        }

    }


    class Messages_manager
    {
        private ArrayList allMessages = new ArrayList();
        private Messages_manager()
        { }
        static Messages_manager messagemanager;
        public static Messages_manager object_existance()
        {
            if (messagemanager == null)
            {
                messagemanager = new Messages_manager();
            }
            return messagemanager;
        }

        public void add_message(string message, string sender_name, string reciever_name)
        {
            Messages message_object = new Messages(message);
            message_object.set_receiver(reciever_name);
            message_object.set_sender(sender_name);

            allMessages.Add(message_object);
        }

        public ArrayList view_all_message(string active_user)
        {
            ArrayList messages_received = new ArrayList();

            for (int x = 0; x < allMessages.Count; x++)
            {
                Messages temp = (Messages)allMessages[x];
                if (temp.get_receiver() == active_user)
                {

                    messages_received.Add(allMessages[x]);
                }

            }
            return messages_received;
        }



    }


    class Program
    {

        static void Main(string[] args)
        {   ///adding demo data
            //ADMIN
            string admin_security_response;
            UserCrud temp = UserCrud.object_existance();
            admin_security_response = temp.newAdmin_security("ADMINOK1234");
            if (admin_security_response == "VALID")
            {
                temp.add_users("MUSAWIR", "1234", "ADMIN");
            }
            //
            //USER
            temp.add_users("SHAN", "1234", "USER");
            temp.add_users("SAFE", "1234", "USER");
            ///
            Program program_object = new Program();
            int option = 0;
            while (option != 3)
            {
                Console.Clear();
                program_object.main_menu();
                option = int.Parse(Console.ReadLine());
                if (option == 1)
                {
                    program_object.signin();
                }
                if (option == 2)
                {
                    program_object.signup();
                }

            }
        }

        void signup()
        {
            UserCrud temp = UserCrud.object_existance();
            string username;
            string password;
            String category;
            String returned_message;
            Console.WriteLine("ENTER YOUR USERNAME =");
            username = Console.ReadLine();
            Console.WriteLine("ENTER YOUR PASSWORD =");
            password = Console.ReadLine();
            Console.WriteLine("ENTER YOUR CATEGORY ADMIN / USER =");
            category = Console.ReadLine();
            if (category == "ADMIN")
            {
                string pinn;
                string admin_security_response;
                Console.Write("ENTER ADMIN SECURITY PASS =");
                pinn = Console.ReadLine();
                admin_security_response = temp.newAdmin_security(pinn);
                if (admin_security_response == "VALID")
                {
                    returned_message = temp.add_users(username, password, category);
                    Console.WriteLine(returned_message);
                }
                else
                {
                    Console.WriteLine("INVALID ADMIN SECURITY KEY ENTERED");
                }
                press_key();
            }
            else
            {
                returned_message = temp.add_users(username, password, category);
                Console.WriteLine(returned_message);
                Console.ReadLine();
            }
        }

        void signin()
        {
            UserCrud user_crud_object = UserCrud.object_existance();
            string username;
            string password;
            string user_type;
            Console.Write("ENTER YOUR USERNAME =");
            username = Console.ReadLine();
            Console.Write("ENTER YOUR PASSWORD =");
            password = Console.ReadLine();
            user_type = user_crud_object.user_verification(username, password);
            if (user_type == "ADMIN")
            {
                admin();
            }

            else if (user_type != "USER NOT FOUND")
            {

                user(user_type);

            }

            else if (user_type == "USER NOT FOUND")
            {

                Console.WriteLine("INVALID USER ");
                press_key();
            }

        }

        void admin()
        {
            UserCrud user_crud_object = UserCrud.object_existance();
            int admin_option = 6;
            while (admin_option != 3)
            {
                header();
                admin_menu();
                admin_option = int.Parse(Console.ReadLine());
                if (admin_option == 1)
                {
                    view_all_users_admin(user_crud_object);

                }

                if (admin_option == 2)
                {
                    update_pinn_user(user_crud_object);
                }
            }
        }

        void view_all_users_admin(UserCrud user_crud_object)
        {
            ArrayList temp = new ArrayList();
            temp = user_crud_object.viewAll_users();
            header();
            Console.WriteLine("USER NAME " + "\t" + "PINN" + "\t" + "CATEGORY");
            for (int x = 0; x < temp.Count; x++)
            {
                User attributes = (User)temp[x];
                Console.WriteLine(attributes.get_username() + "\t\t" + attributes.get_password() + "\t" + attributes.get_user_category());
            }
            press_key();
        }

        void update_pinn_user(UserCrud user_crud_object)
        {
            string username;
            string pinn;
            String return_message;
            Console.Write("ENTER USERNAME OF THE USER OF WHICH YOU WANT TO CHANGE PINN =");
            username = Console.ReadLine();
            Console.WriteLine("ENTER NEW PINN =");
            pinn = Console.ReadLine();
            return_message = user_crud_object.update_pinn(username, pinn);
            Console.WriteLine(return_message);
            press_key();
        }
        void main_menu()
        {
            header();
            Console.WriteLine("1.\tLOGIN");
            Console.WriteLine("2.\tSIGNUP");
            Console.WriteLine("3.\tEXIT\n");
            Console.Write("ENTER OPTION NUMBER =");
        }

        void admin_menu()
        {
            header();
            Console.WriteLine("1.\tVIEW ALL USER");
            Console.WriteLine("2.\tCHANGE PINN");
            Console.WriteLine("3.\tEXIT\n");
            Console.Write("ENTER OPTION NUMBER =");

        }

        void user(string user_type)
        {
            UserCrud user_crud_object = UserCrud.object_existance();
            Messages_manager message_send_object = Messages_manager.object_existance();

            int user_option = 6;
            while (user_option != 3)
            {
                user_menu(user_type);
                user_option = int.Parse(Console.ReadLine());

                if (user_option == 1)
                {
                    send_message(user_type, user_crud_object, message_send_object);

                }
                if (user_option == 2)
                {
                    receive_messages(user_type, user_crud_object, message_send_object);
                }
            }

        }
        void send_message(string user_type, UserCrud user_crud_object, Messages_manager message_send_object)
        {
            string message;
            string sender_name;
            string receiver_name;
            string receiver_verification;
            Console.Write("ENTER YOUR MESSAGE =");
            message = Console.ReadLine();
            Console.Write("ENTER RECEIVER NAME =");
            receiver_name = Console.ReadLine();
            sender_name = user_type;

            receiver_verification = user_crud_object.user_verification(receiver_name, "RECIEVER_VERIFICATION");
            if (receiver_verification == "USER")
            {
                message_send_object.add_message(message, sender_name, receiver_name);
                Console.Clear();
                Console.WriteLine("MESSAGE SENT SUCESSFULLY");
            }
            else
            {
                Console.WriteLine("MESSAGE NOT SENT");
                Console.WriteLine("PROVIDED INORMATION MUST BE WRONG");

            }
            press_key();
        }
        void receive_messages(string user_type, UserCrud user_crud_object, Messages_manager message_send_object)
        {
            ArrayList messages_received = new ArrayList();

            messages_received = message_send_object.view_all_message(user_type);
            Console.WriteLine("SENDER NAME" + "\t\t" + "MESSAGES");
            if (messages_received.Count == 0)
            {
                Console.WriteLine("INBOX IS EMPTY");
            }
            else
            {
                for (int x = 0; x < messages_received.Count; x++)
                {
                    Messages attributes = (Messages)messages_received[x];
                    Console.WriteLine(attributes.get_sender() + "\t\t" + attributes.get_message());
                }
            }
            press_key();
        }
        void user_menu(String user_type)
        {
            header();
            Console.WriteLine("USER >>> " + user_type);
            Console.WriteLine("1.\tSEND MESSAGE");
            Console.WriteLine("2.\tRECIEVE MESSAGE");
            Console.WriteLine("3.\tEXIT\n");
            Console.Write("ENTER OPTION NUMBER...=");
        }

        void header()
        {
            Console.Clear();
            Console.WriteLine("********************************************************************");
            Console.WriteLine("*                           MESSAGING SYSTEM                       *");
            Console.WriteLine("******************************************************************** \n ");
            Console.WriteLine(">> WELCOME >> \n");

        }
        void press_key()
        {
            Console.WriteLine("PRESS ANY KE TO CONTINUE......................");
            Console.ReadLine();
        }

    }
}
