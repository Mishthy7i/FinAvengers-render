import 'package:http/http.dart' as http;
import 'dart:convert';
import 'package:shared_preferences/shared_preferences.dart';

class TransactionService {
  static const String _baseUrl = 'https://finavengers-render.onrender.com';

  Future<List<Map<String, dynamic>>> fetchTransactions() async {
    final prefs = await SharedPreferences.getInstance();
    final token = prefs.getString('jwt_token');

    final response = await http.get(
      Uri.parse('$_baseUrl/transactions/'),
      headers: {'Authorization': 'Bearer $token'},
    );

    if (response.statusCode == 200) {
      return List<Map<String, dynamic>>.from(jsonDecode(response.body));
    }
    throw Exception('Failed to fetch transactions');
  }

  Future<bool> addTransaction(Map<String, dynamic> transactionData) async {
    final prefs = await SharedPreferences.getInstance();
    final token = prefs.getString('jwt_token');

    final response = await http.post(
      Uri.parse('$_baseUrl/transactions/add'),
      headers: {
        'Authorization': 'Bearer $token',
        'Content-Type': 'application/json',
      },
      body: jsonEncode(transactionData),
    );

    return response.statusCode == 200;
  }
}
