from sprite_object import *
from npc import *

class ObjectHandler:
    def __init__(self, game):
        self.game = game
        self.sprite_list = []
        self.npc_list = []
        self.npc_sprite_path = "resources/sprites/npc/"
        self.static_sprite_path = "resources/sprites/static_sprites/"
        self.anim_sprite_path = "resources/sprites/animated_sprites/"
        add_sprite = self.add_sprite
        add_npc = self.add_npc
        self.npc_positions = {}

        #sprite map
        add_sprite(SpriteObject(game))
        add_sprite(AnimatedSprite(game, pos=(1.1, 1.1)))
        add_sprite(AnimatedSprite(game, pos=(15.9, 1.1)))
        add_sprite(AnimatedSprite(game, pos=(15.9, 8.9)))
        add_sprite(AnimatedSprite(game, path=self.anim_sprite_path + "red_light/0.png", pos=(10.1, 4.1)))
        add_sprite(AnimatedSprite(game, path=self.anim_sprite_path + "red_light/0.png", pos=(3.8, 5.5)))
        add_sprite(AnimatedSprite(game, path=self.anim_sprite_path + "red_light/0.png", pos=(11.8, 2.8)))
        add_sprite(AnimatedSprite(game, path=self.anim_sprite_path + "red_light/0.png", pos=(7.5, 4.1)))

        #npc map
        add_npc(NPC(game))
        add_npc(NPC(game, pos=(11.5, 4.5)))
        add_npc(CyberDemonNPC(game, pos=(15.9, 1.1)))
        add_npc(CacoDemonNPC(game, pos=(15.9, 8.9)))
        add_npc(CacoDemonNPC(game, pos=(15.9, 8.9)))
        add_npc(CacoDemonNPC(game, pos=(15.9, 8.9)))
        add_npc(CacoDemonNPC(game, pos=(15.9, 8.9)))
        add_npc(CacoDemonNPC(game, pos=(15.9, 8.9)))

    def check_win(self):
        if not(self.npc_positions):
            self.game.object_renderer.win()
            pg.display.flip()
            pg.time.delay(1500)
            self.game.new_game()

    def update(self):
        self.npc_positions = {npc.map_pos for npc in self.npc_list if npc.alive}
        [sprite.update() for sprite in self.sprite_list]
        [npc.update() for npc in self.npc_list]
        self.check_win()

    def add_npc(self, npc):
        self.npc_list.append(npc)

    def add_sprite(self, sprite):
        self.sprite_list.append(sprite)