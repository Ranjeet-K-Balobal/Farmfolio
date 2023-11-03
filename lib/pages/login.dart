import 'package:flutter/material.dart';

class LoginPage extends StatefulWidget {
  const LoginPage({Key? key});

  @override
  _LoginPageState createState() => _LoginPageState();
}

class _LoginPageState extends State<LoginPage> {
  final TextEditingController usernameController = TextEditingController();
  final TextEditingController passwordController = TextEditingController();
  String selectedRole = 'Banker'; // Default role

  // Function to handle the login button press
  void _login() {
    final username = usernameController.text;
    final password = passwordController.text;

    // Implement your authentication logic here
    // Check if the username and password are valid

    // For demonstration, we'll just print the role and credentials
    print('Role: $selectedRole');
    print('Username: $username');
    print('Password: $password');

    // You can add logic to navigate to the appropriate page based on the role
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text('Login Page'),
        backgroundColor: Colors.blue, // Set the app bar background color
      ),
      body: Center(
        child: Padding(
          padding: const EdgeInsets.all(16.0),
          child: Column(
            mainAxisAlignment: MainAxisAlignment.center,
            children: <Widget>[
              DropdownButton<String>(
                value: selectedRole,
                items: <String>[
                  'Banker',
                  'Farmer',
                  'Other Roles', // Add more role options if needed
                ].map((String value) {
                  return DropdownMenuItem<String>(
                    value: value,
                    child: Text(value),
                  );
                }).toList(),
                onChanged: (String? newValue) {
                  setState(() {
                    selectedRole = newValue ?? 'Banker'; // Use a default value if null
                  });
                },
                style: TextStyle(
                  color: Colors.blue, // Set the text color of the dropdown
                ),
                dropdownColor: Colors.white, // Set the dropdown background color
              ),
              const SizedBox(height: 20.0), // Increased spacing
              TextField(
                controller: usernameController,
                decoration: InputDecoration(
                  labelText: 'Username',
                  border: OutlineInputBorder(), // Add input field border
                ),
              ),
              const SizedBox(height: 10.0), // Adjusted spacing
              TextField(
                controller: passwordController,
                obscureText: true,
                decoration: InputDecoration(
                  labelText: 'Password',
                  border: OutlineInputBorder(),
                ),
              ),
              const SizedBox(height: 20.0), // Increased spacing
              ElevatedButton(
                onPressed: _login,
                child: const Text('Login'),
                style: ElevatedButton.styleFrom(
                  primary: Colors.blue, // Set the button background color
                ),
              ),
            ],
          ),
        ),
      ),
    );
  }
}
