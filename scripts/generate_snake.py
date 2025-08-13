name: Generate Snake Animation

on:
  schedule:
    - cron: "0 12 * * *"  # Executa diariamente ao meio-dia UTC
  workflow_dispatch:
  push:
    branches: [ "main" ]

jobs:
  generate:
    runs-on: ubuntu-latest
    permissions:
      contents: write
      
    steps:
      - uses: actions/checkout@v4
      
      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: "3.10"
          
      - name: Install dependencies
        run: pip install github-contribution-snake
          
      - name: Generate snake
        run: |
          mkdir -p dist
          github-contribution-snake -u ${{ github.repository_owner }} -o dist/snake.svg
          
      - name: Commit and push
        run: |
          git config --global user.name "GitHub Actions"
          git config --global user.email "actions@github.com"
          git add dist/
          git commit -m "Update snake animation [skip ci]"
          git push
