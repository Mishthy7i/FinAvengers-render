import 'package:flutter/material.dart';
import 'package:flutter_jwt/services/auth_service.dart';
import 'package:flutter_jwt/services/transaction_service.dart';

class HomePage extends StatefulWidget {
  const HomePage({Key? key}) : super(key: key);

  @override
  _HomePageState createState() => _HomePageState();
}

class _HomePageState extends State<HomePage> {
  final TransactionService _transactionService = TransactionService();
  final AuthService _authService = AuthService();
  List<Map<String, dynamic>> _transactions = [];

  Future<void> _fetchTransactions() async {
    try {
      final transactions = await _transactionService.fetchTransactions();
      setState(() {
        _transactions = transactions;
      });
    } catch (e) {
      ScaffoldMessenger.of(context).showSnackBar(
        const SnackBar(content: Text('Failed to fetch transactions')),
      );
    }
  }

  Future<void> _addTransaction(Map<String, dynamic> transactionData) async {
    final success = await _transactionService.addTransaction(transactionData);
    if (success) {
      await _fetchTransactions();
      Navigator.pop(context);
    } else {
      ScaffoldMessenger.of(context).showSnackBar(
        const SnackBar(content: Text('Failed to add transaction')),
      );
    }
  }

  @override
  void initState() {
    super.initState();
    _fetchTransactions();
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text('Home'),
        actions: [
          IconButton(
            icon: const Icon(Icons.logout),
            onPressed: () async {
              await _authService.logout();
              Navigator.pushReplacementNamed(context, '/splash');
            },
          ),
        ],
        automaticallyImplyLeading: false, // Disable back button
      ),
      body: ListView.builder(
        itemCount: _transactions.length,
        itemBuilder: (context, index) {
          final transaction = _transactions[index];
          return ListTile(
            title: Text(
              '${transaction['category']} - ${transaction['amount']}',
            ),
            subtitle: Text(transaction['mode']),
          );
        },
      ),
      floatingActionButton: FloatingActionButton(
        onPressed: () {
          showDialog(
            context: context,
            builder: (context) {
              final _amountController = TextEditingController();
              final _categoryController = TextEditingController();
              final _modeController = TextEditingController();

              return AlertDialog(
                title: const Text('Add Transaction'),
                content: Column(
                  mainAxisSize: MainAxisSize.min,
                  children: [
                    TextField(
                      controller: _amountController,
                      decoration: const InputDecoration(labelText: 'Amount'),
                    ),
                    TextField(
                      controller: _categoryController,
                      decoration: const InputDecoration(labelText: 'Category'),
                    ),
                    TextField(
                      controller: _modeController,
                      decoration: const InputDecoration(labelText: 'Mode'),
                    ),
                  ],
                ),
                actions: [
                  TextButton(
                    onPressed: () {
                      Navigator.pop(context);
                    },
                    child: const Text('Cancel'),
                  ),
                  ElevatedButton(
                    onPressed: () async {
                      final transactionData = {
                        'amount':
                            double.tryParse(_amountController.text) ?? 0.0,
                        'category': _categoryController.text,
                        'mode': _modeController.text,
                      };
                      await _addTransaction(transactionData);
                    },
                    child: const Text('Add'),
                  ),
                ],
              );
            },
          );
        },
        child: const Icon(Icons.add),
      ),
    );
  }
}
