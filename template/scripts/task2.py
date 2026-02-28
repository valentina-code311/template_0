import argparse

def main():
  parser = argparse.ArgumentParser(description="Task 2")
  parser.add_argument("project_name", help="Name of the project")
  parser.add_argument("destination", help="Destination directory")
  args = parser.parse_args()

  print(f"✅ Proyecto '{args.project_name}' creado correctamente en '{args.destination}'.")

if __name__ == "__main__":
  main()
