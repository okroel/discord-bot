class WalletManager(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def add_address(self, ctx, wallet_address, network='ETH'):
        await ctx.send("Hello")


