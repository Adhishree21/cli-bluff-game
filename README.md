# CLI Bluff Card Game 🂡

A command-line implementation of the classic **Bluff** (also known as **Cheat** or **BS**) card game. Challenge your friends in this strategic game of deception where you try to get rid of all your cards first!

## 🎯 Game Overview

**Bluff** is a card game where players take turns playing cards face-down while declaring what rank they're playing. The catch? You can lie about what you're actually playing! Other players can challenge you if they suspect you're bluffing.

**Objective:** Be the first player to get rid of all your cards.


### Installation & Running

1. **Clone this repository:**
   ```bash
   git clone https://github.com/Adhishree21/cli-bluff-game.git
   cd cli-bluff-game
   ```

2. **Run the game:**
   ```bash
   python bluff_game.py
   ```

## 🎮 How to Play

### Game Setup
1. Run the game and enter number of players (2-6)
2. Cards are automatically dealt to all players
3. Each player starts with an equal number of cards

### Game Flow
1. **Your Turn:** Look at your hand organized by rank
2. **Declare Rank:** Choose what rank you claim to be playing
3. **Select Cards:** Pick which cards from your hand to play
4. **Challenge Phase:** The next player can challenge your claim
5. **Resolution:** If challenged, cards are revealed

### Key Rules
- **First Turn:** Any player can start with any rank
- **Following Turns:** Must play the same rank OR pass
- **Passing:** If everyone passes, the rank resets
- **Challenging:** Next player can challenge if they suspect a bluff
- **Bluff Detected:** Bluffer takes all cards in the center pile
- **No Bluff:** Challenger takes all cards in the center pile

## 🔧 Common Issues & Solutions

### Issue 1: Input Issues During Game
**Problem:** Game asks for input but seems stuck
**Solution:** 
- Make sure to press Enter after typing
- For card selection, use format: `1,3,5` (numbers with commas)
- For yes/no questions, type `yes` or `no` (not y/n)

### Issue 2: Invalid Card Selection
**Problem:** "Invalid index" error when selecting cards
**Solution:** 
- Use the numbers shown next to cards (1, 2, 3, etc.)
- Separate multiple selections with commas: `1,2,4`
- Don't use spaces around commas: `1,2,3` ✅ not `1, 2, 3` ❌

## 💡 Pro Tips

### Strategic Play
- **Bluffing:** Don't always tell the truth - that's the fun!
- **Card Counting:** Pay attention to what ranks have been played
- **Challenge Timing:** Challenge when you suspect but aren't certain
- **Hand Management:** Sometimes it's better to pass than play

### Input Tips
- **Card Selection:** You can select multiple cards: `1,3,5,7`
- **Passing:** When it's not your starting turn, you can pass if you don't have (or don't want to play) the current rank
- **Rank Declaration:** Use standard notation: `2,3,4,5,6,7,8,9,10,J,Q,K,A`

## 🎲 Game Features

- ✅ 2-6 players support
- ✅ Automatic card shuffling and dealing
- ✅ Hand organization by rank for easy viewing
- ✅ Clear turn indicators and game state
- ✅ Challenge system with reveal mechanics
- ✅ Automatic win detection
- ✅ Pass system when you can't/don't want to play

## 🐛 Known Issues

1. **Terminal Width:** Very long hands might wrap awkwardly on narrow terminals
2. **Input Validation:** Some edge cases in card selection might cause errors
3. **Unicode Support:** Card suits might not display correctly on all systems

## 🤝 Contributing

Found a bug or want to add a feature? Contributions welcome!

1. Fork the repository
2. Create a feature branch: `git checkout -b feature-name`
3. Make changes and test thoroughly
4. Commit: `git commit -m "Add feature description"`
5. Push: `git push origin feature-name`
6. Create a Pull Request.


## 🎉 Acknowledgments

- Classic Bluff/Cheat card game rules
- Python community for excellent documentation
- All players who helped test this implementation

---

**Enjoy the game and happy bluffing! 🃏**


