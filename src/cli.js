#!/usr/bin/env node

import { Command } from 'commander';
import chalk from 'chalk';
import { fileURLToPath } from 'url';
import { dirname } from 'path';

const __filename = fileURLToPath(import.meta.url);
const __dirname = dirname(__filename);

const program = new Command();

program
  .name('my-cli-tool')
  .description('A powerful CLI tool for everyday tasks')
  .version('1.0.0');

// Add your commands here
program
  .command('hello')
  .description('Say hello to the world')
  .action(() => {
    console.log(chalk.green('Hello, World! 👋'));
  });

program
  .command('info')
  .description('Show tool information')
  .action(() => {
    console.log(chalk.blue('My CLI Tool v1.0.0'));
    console.log(chalk.gray('A starter template for building CLI tools'));
  });

program.parse();
