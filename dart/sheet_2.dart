int maxOfThree(int a, int b, int c) {
  if (a > b && a > c) {
    return a;
  } else if (b > c) {
    return b;
  } else {
    return c;
  }
}

void main() {
  List<int> test = [1, 2, 3];
  int max = maxOfThree(test[0], test[1], test[2]);
  print("test $test | max number: $max");
  test = [3, 2, 1];
  max = maxOfThree(test[0], test[1], test[2]);
  print("test $test | max number: $max");
  test = [1, 3, 2];
  max = maxOfThree(test[0], test[1], test[2]);
  print("test $test | max number: $max");
  test = [1, 3, 3];
  max = maxOfThree(test[0], test[1], test[2]);
  print("test $test | max number: $max");
  test = [3, 3, 3];
  max = maxOfThree(test[0], test[1], test[2]);
  print("test $test | max number: $max");
}
