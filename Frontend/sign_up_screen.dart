import 'package:flutter/material.dart';

class SignUpScreen extends StatefulWidget {
  final Function(String, String) onRegister;
  const SignUpScreen({super.key, required this.onRegister});

  @override
  State<SignUpScreen> createState() => _SignUpScreenState();
}

class _SignUpScreenState extends State<SignUpScreen> {
  final emailController = TextEditingController();
  final passwordController = TextEditingController();
  final confirmPasswordController = TextEditingController();
  String? errorMessage;

  void handleSignUp() {
    final email = emailController.text;
    final pass = passwordController.text;
    final confirmPass = confirmPasswordController.text;

    if (email.isEmpty || pass.isEmpty || pass != confirmPass) {
      setState(() => errorMessage = "Invalid Credentials");
    } else {
      widget.onRegister(email, pass);
      setState(() => errorMessage = null);
      Navigator.pop(context);
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
            const Text("Sign up to FinQuest", style: TextStyle(fontSize: 20)),
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
            TextField(
              controller: confirmPasswordController,
              obscureText: true,
              decoration: const InputDecoration(labelText: "Confirm Password"),
            ),
            const SizedBox(height: 10),
            const Text("By continuing you agree to our terms & conditions.",
                style: TextStyle(fontSize: 10)),
            const SizedBox(height: 10),
            ElevatedButton(
                onPressed: handleSignUp, child: const Text("Sign up")),
            TextButton(
              onPressed: () => Navigator.pop(context),
              child: const Text("Already have an account? Sign-in"),
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

