import 'dart:io';

Map days = {
  0: [],
  1: ["C++ 10:00Am", "Python 11:30Am"],
  2: ["Database 9:00Am"],
  3: ["Vacation"],
  4: [],
  5: ["Web 1:00Pm", "ML 11:30Am"],
  6: ["Dart 10:00Am", "SE 11:30Am"],
};

int getInput() {
  print("""\n\n
    [1] Saturday
    [2] Sunday
    [3] Monday
    [4] Tuesday
    [5] Wednesday
    [6] Thursday
    Plase select number of day (0 to Exit): 
""");

  return int.tryParse(stdin.readLineSync() ?? '') ?? -1;
}

void printOutput(int day) {
  for (var sec in days[day]) {
    print(sec);
  }
}

void main() {
  int day;
  
  do {
    day = getInput();
    if (day == -1) {
      print("plase Enter a number like 1 to Saturday");
      continue;
    }
    if (day < 0 || day > 6) {
      print("plase Enter a number bettwen 1 -> 7");
      continue;
    }
    printOutput(day);
  } while (day != 0);
}
