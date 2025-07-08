import 'package:flutter/material.dart';

class ResetPasswordScreen extends StatefulWidget {
  const ResetPasswordScreen({super.key});

  @override
  State<ResetPasswordScreen> createState() => _ResetPasswordScreenState();
}

class _ResetPasswordScreenState extends State<ResetPasswordScreen> {
  final emailController = TextEditingController();
  bool linkSent = false;

  void sendLink() {
    setState(() => linkSent = true);
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
            const Text("Reset Password", style: TextStyle(fontSize: 20)),
            const SizedBox(height: 20),
            TextField(
              controller: emailController,
              decoration: const InputDecoration(labelText: "Email"),
            ),
            const SizedBox(height: 8),
            const Text("This will email you a link to reset your password.",
                style: TextStyle(fontSize: 12)),
            const SizedBox(height: 10),
            ElevatedButton(onPressed: sendLink, child: const Text("Send")),
            if (linkSent)
              Container(
                color: Colors.green,
                width: double.infinity,
                padding: const EdgeInsets.all(8),
                child: const Text("Link sent successfully",
                    style: TextStyle(color: Colors.white),
                    textAlign: TextAlign.center),
              ),
          ]),
        ),
      ),
    );
  }
}
