import 'package:flutter/material.dart';
import 'package:go_router/go_router.dart';

final appRouter = GoRouter(
  initialLocation: '/',
  routes: [
    GoRoute(
      path: '/',
      name: AppRouteNames.home,
      builder: (context, state) => const HomePage(),
    ),
    GoRoute(
      path: '/login',
      name: AppRouteNames.login,
      builder: (context, state) => const LoginPage(),
    ),
  ],
  errorBuilder: (context, state) => ErrorPage(error: state.error),
);

class AppRouteNames {
  const AppRouteNames._();

  static const home = 'home';
  static const login = 'login';
}

// Replace these placeholders with real pages.
class HomePage extends StatelessWidget {
  const HomePage({super.key});

  @override
  Widget build(BuildContext context) => const Scaffold(
        body: Center(child: Text('Home')),
      );
}

class LoginPage extends StatelessWidget {
  const LoginPage({super.key});

  @override
  Widget build(BuildContext context) => const Scaffold(
        body: Center(child: Text('Login')),
      );
}

class ErrorPage extends StatelessWidget {
  const ErrorPage({super.key, this.error});

  final Exception? error;

  @override
  Widget build(BuildContext context) => Scaffold(
        body: Center(
          child: Text(error?.toString() ?? 'Page not found'),
        ),
      );
}
