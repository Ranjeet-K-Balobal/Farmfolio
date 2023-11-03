import 'package:flutter/material.dart';
import 'home_page.dart';

class LoginPage extends StatefulWidget {
  const LoginPage({Key? key}) : super(key: key);

  @override
  _LoginPageState createState() => _LoginPageState();
}

class _LoginPageState extends State<LoginPage> {
  final TextEditingController usernameController = TextEditingController();
  final TextEditingController passwordController = TextEditingController();
  String selectedRole = 'Banker'; // Default role

  void _login() {
    final username = usernameController.text;
    final password = passwordController.text;

    print('Role: $selectedRole');
    print('Username: $username');
    print('Password: $password');

    // Navigate to the appropriate home page based on the role
    if (selectedRole == 'Banker') {
      Navigator.push(
        context,
        MaterialPageRoute(builder: (context) => HomePage(role: 'Banker')),
      );
    } else {
      Navigator.push(
        context,
        MaterialPageRoute(builder: (context) => HomePage(role: 'Farmer')),
      );
    }
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text('Login Page'),
        backgroundColor: Colors.blue,
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
                  'Other Roles',
                ].map((String value) {
                  return DropdownMenuItem<String>(
                    value: value,
                    child: Text(value),
                  );
                }).toList(),
                onChanged: (String? newValue) {
                  setState(() {
                    selectedRole = newValue ?? 'Banker';
                  });
                },
                style: TextStyle(
                  color: Colors.blue,
                ),
                dropdownColor: Colors.white,
              ),
              const SizedBox(height: 20.0),
              TextField(
                controller: usernameController,
                decoration: InputDecoration(
                  labelText: 'Username',
                  border: OutlineInputBorder(),
                ),
              ),
              const SizedBox(height: 10.0),
              TextField(
                controller: passwordController,
                obscureText: true,
                decoration: InputDecoration(
                  labelText: 'Password',
                  border: OutlineInputBorder(),
                ),
              ),
              const SizedBox(height: 20.0),
              ElevatedButton(
                onPressed: _login,
                child: const Text('Login'),
                style: ElevatedButton.styleFrom(
                  primary: Colors.blue,
                ),
              ),
            ],
          ),
        ),
      ),
    );
  }
}
