import 'package:flutter/material.dart';
import 'reset_password_screen.dart';
import 'sign_up_screen.dart';

class SignInScreen extends StatefulWidget {
  const SignInScreen({super.key});

  @override
  State<SignInScreen> createState() => _SignInScreenState();
}

class _SignInScreenState extends State<SignInScreen> {
  final emailController = TextEditingController();
  final passwordController = TextEditingController();

  String? errorMessage;
  Map<String, String> users = {};

  void register(String email, String password) {
    users[email] = password;
  }

  void handleLogin() {
    final email = emailController.text;
    final pass = passwordController.text;

    if (users[email] != pass) {
      setState(() => errorMessage = "Invalid Credentials");
    } else {
      setState(() => errorMessage = null);
      ScaffoldMessenger.of(context)
          .showSnackBar(const SnackBar(content: Text("Login Successful")));
    }
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: Center(
        child: Container(
          width: 320,
          padding: const EdgeInsets.all(20),
          child: Column(mainAxisSize: MainAxisSize.min, children: [
            const SizedBox(height: 40),
            const Text("Sign in to FinQuest", style: TextStyle(fontSize: 20)),
            const SizedBox(height: 20),
            TextField(
              controller: emailController,
              decoration: const InputDecoration(labelText: "Email"),
            ),
            TextField(
              controller: passwordController,
              obscureText: true,
              decoration: const InputDecoration(labelText: "Password"),
            ),
            const SizedBox(height: 10),
            ElevatedButton(
                onPressed: handleLogin, child: const Text("Sign in")),
            TextButton(
              onPressed: () {
                Navigator.push(
                  context,
                  MaterialPageRoute(
                      builder: (_) => const ResetPasswordScreen()),
                );
              },
              child: const Text("Forgot Password?"),
            ),
            TextButton(
              onPressed: () {
                Navigator.push(
                  context,
                  MaterialPageRoute(
                    builder: (_) => SignUpScreen(onRegister: register),
                  ),
                );
              },
              child: const Text("Don't have an account? Sign-up"),
            ),
            if (errorMessage != null)
              Container(
                color: Colors.red,
                width: double.infinity,
                padding: const EdgeInsets.all(8),
                child: Text(errorMessage!,
                    style: const TextStyle(color: Colors.white),
                    textAlign: TextAlign.center),
              ),
          ]),
        ),
      ),
    );
  }
}

