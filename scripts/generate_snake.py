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
      
      - uses: Platane/snk@master
        with:
          github_user_name: ${{ github.repository_owner }}
          outputs: |
            dist/github-contribution-snake.svg
            dist/github-contribution-snake-dark.svg?palette=github-dark
          
      - name: Commit and push
        run: |
          git config --global user.name "GitHub Actions"
          git config --global user.email "actions@github.com"
          git add dist/
          git commit -m "Update snake animation [skip ci]"
          git push
