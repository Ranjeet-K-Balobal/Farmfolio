import 'package:flutter/material.dart';

class HomePage extends StatelessWidget {
  final String role;

  HomePage({required this.role});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text('$role Home Page'),
      ),
      body: Center(
        child: Text('Welcome, $role!'),
      ),
    );
  }
}
