from rest_framework import serializers

from lib.pyffish import xiangqi
from xiangqi.models import DrawEvent, Game, Player, TakebackEvent
from xiangqi.models.team import Team
from xiangqi.serializers.move_serializer import MoveSerializer, PositionSerializer
from xiangqi.serializers.player_serializer import PlayerSerializer


class GameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = ["slug", "moves", "player1", "score1", "player2", "score2"]

    moves = MoveSerializer(source="move_set", many=True, read_only=True)
    player1 = serializers.SlugRelatedField("username", queryset=Player.objects.all())
    player2 = serializers.SlugRelatedField("username", queryset=Player.objects.all())

    def to_representation(self, instance):
        result = super().to_representation(instance)
        self._transform_moves(result)
        self._transform_players(result, instance)
        self._add_open_draw_offer(result, instance)
        self._add_open_takeback_offer(result, instance)
        return result

    def _transform_moves(self, result):
        start_position = PositionSerializer(data={"fen": xiangqi.start_fen()})
        start_position.is_valid(raise_exception=True)
        result["moves"] = [start_position.data] + result["moves"]

    def _transform_players(self, result, instance):
        result["player1"] = {
            "team": Team.RED.value,
            **PlayerSerializer(instance.player1).data,
        }
        result["player2"] = {
            "team": Team.BLACK.value,
            **PlayerSerializer(instance.player2).data,
        }

    def _add_open_draw_offer(self, result, instance):
        result["open_draw_offer"] = None

        first_open_offer = (
            DrawEvent.open_offers.filter(game=instance).order_by("created_at").first()
        )
        if first_open_offer:
            result["open_draw_offer"] = first_open_offer.payload["username"]

    def _add_open_takeback_offer(self, result, instance):
        result["open_takeback_offer"] = None

        first_open_offer = (
            TakebackEvent.open_offers.filter(game=instance)
            .order_by("created_at")
            .first()
        )
        if first_open_offer:
            result["open_takeback_offer"] = first_open_offer.payload["username"]
